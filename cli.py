import sys
from pathlib import Path
from typing import Optional, List, Dict, Any
import config
from database import BirdDatabase
from bird_info import BirdInfoRepository, BIRD_KNOWLEDGE_BASE
from image_classifier import BirdImageClassifier
from audio_classifier import BirdAudioClassifier
from comparison import compare_modalities, compare_two_birds
from exporter import export_to_csv, compute_statistics, generate_distribution_chart
from batch_runner import BatchRunner

class BirdLabCLI:
    def __init__(self):
        self.db = BirdDatabase(config.DATABASE_PATH)
        self.info_repo = BirdInfoRepository()
        self.image_classifier = BirdImageClassifier()
        self.audio_classifier = BirdAudioClassifier()
        self.batch_runner = BatchRunner()

    def run(self) -> None:
        while True:
            self._print_header("AI Bird Lab - Головне меню")
            print("1. Аналіз фотографії птаха")
            print("2. Аналіз аудіозапису співу")
            print("3. Мультимодальний аналіз (фото + аудіо)")
            print("4. Перегляд та пошук у базі даних")
            print("5. Фільтрація бази даних")
            print("6. Видалення запису з бази даних")
            print("7. Порівняння двох видів птахів")
            print("8. Пакетний аналіз тестового набору (15+ фото)")
            print("9. Експорт результатів у CSV та статистика")
            print("0. Вихід")

            choice = input("\nОберіть дію (0-9): ").strip()
            if choice == "1":
                self._handle_image_analysis()
            elif choice == "2":
                self._handle_audio_analysis()
            elif choice == "3":
                self._handle_multimodal_analysis()
            elif choice == "4":
                self._handle_database_search()
            elif choice == "5":
                self._handle_database_filter()
            elif choice == "6":
                self._handle_delete_record()
            elif choice == "7":
                self._handle_species_comparison()
            elif choice == "8":
                self._handle_batch_run()
            elif choice == "9":
                self._handle_export_and_stats()
            elif choice == "0":
                print("\nРоботу програми завершено.")
                break
            else:
                print("\nНекоректний вибір. Спробуйте ще раз.")

    def _print_header(self, text: str) -> None:
        print("\n" + "=" * 60)
        print(f" {text}")
        print("=" * 60)

    def _handle_image_analysis(self) -> None:
        self._print_header("Аналіз фотографії птаха")
        print("Введіть шлях до зображення (або натисніть Enter для вибору зразка):")
        path_input = input("Шлях: ").strip().strip('"').strip("'")

        img_path = None
        if not path_input:
            samples = list(config.SAMPLE_DIR.glob("*.jpg"))
            if not samples:
                print("Зразки не знайдено.")
                return
            print("\nДоступні зразки:")
            for idx, s in enumerate(samples[:10], 1):
                print(f"{idx}. {s.name}")
            sub_choice = input("Оберіть номер зразка: ").strip()
            if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(samples[:10]):
                img_path = samples[int(sub_choice) - 1]
            else:
                print("Некоректний номер.")
                return
        else:
            img_path = Path(path_input)

        if not img_path.exists():
            print(f"Помилка: файл не існує ({img_path})")
            return

        print("\nВиконується інференс моделі...")
        res = self.image_classifier.classify(img_path, top_k=config.TOP_K_PREDICTIONS)
        if not res["success"]:
            print(f"Помилка аналізу: {res['error']}")
            return

        species = res["predicted_species"]
        conf = res["confidence"]
        conf_pct = round(conf * 100, 2)
        info = self.info_repo.find_bird_info(species)

        print("\n" + "-" * 50)
        print(f"Визначений вид: {species}")
        print(f"Впевненість моделі: {conf_pct}%")
        print(f"Українська назва: {info['ukr_name']}")
        print(f"Наукова назва: {info['scientific_name']}")
        print(f"Родина: {info['family']}")
        print(f"Середовище: {info['habitat']}")
        print(f"Ареал: {info['region']}")
        print(f"Живлення: {info['diet']}")
        print(f"Розміри: {info['size']}")
        print(f"Охоронний статус: {info['conservation_status']}")
        print(f"Цікаві факти: {info['interesting_facts']}")

        print("\nТоп-3 найімовірніші варіанти:")
        for idx, v in enumerate(res["variants"], 1):
            pct = round(v["confidence"] * 100, 2)
            print(f"  {idx}. {v['species']} - {pct}%")

        save = input("\nЗберегти цей результат у базу даних? (y/n): ").strip().lower()
        if save in ["y", "yes", "так", "т"]:
            desc = f"{info['ukr_name']} ({info['scientific_name']})"
            add_info = f"Середовище: {info['habitat']}. Статус: {info['conservation_status']}."
            rec_id = self.db.add_record(
                analysis_type="image",
                predicted_species=species,
                confidence=conf,
                image_name=img_path.name,
                description=desc,
                scientific_name=info["scientific_name"],
                family=info["family"],
                habitat=info["habitat"],
                region=info["region"],
                diet=info["diet"],
                top3_list=res["variants"],
                additional_info=add_info
            )
            print(f"Запис успішно додано під номером {rec_id}.")

    def _handle_audio_analysis(self) -> None:
        self._print_header("Аналіз аудіозапису співу")
        print("Введіть шлях до аудіофайлу WAV (або натисніть Enter для вибору зразка):")
        path_input = input("Шлях: ").strip().strip('"').strip("'")

        aud_path = None
        if not path_input:
            samples = list(config.SAMPLE_DIR.glob("*.wav"))
            if not samples:
                print("Аудіозразки не знайдено.")
                return
            print("\nДоступні зразки:")
            for idx, s in enumerate(samples, 1):
                print(f"{idx}. {s.name}")
            sub_choice = input("Оберіть номер зразка: ").strip()
            if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(samples):
                aud_path = samples[int(sub_choice) - 1]
            else:
                print("Некоректний номер.")
                return
        else:
            aud_path = Path(path_input)

        if not aud_path.exists():
            print(f"Помилка: файл не існує ({aud_path})")
            return

        print("\nВиконується аудіокласифікація...")
        res = self.audio_classifier.classify(aud_path)
        if not res["success"]:
            print(f"Помилка: {res['error']}")
            return

        species = res["predicted_species"]
        conf_pct = round(res["confidence"] * 100, 2)
        info = self.info_repo.find_bird_info(species)

        print("\n" + "-" * 50)
        print(f"Визначений вид: {species}")
        print(f"Впевненість моделі: {conf_pct}%")
        print(f"Статус результату: {res['status_description']}")
        print(f"Українська назва: {info['ukr_name']}")
        print(f"Наукова назва: {info['scientific_name']}")
        print(f"Родина: {info['family']}")

        print("\nВаріанти розпізнавання:")
        for idx, v in enumerate(res["variants"], 1):
            pct = round(v["confidence"] * 100, 2)
            print(f"  {idx}. {v['species']} - {pct}%")

        save = input("\nЗберегти результат аудіоаналізу у базу даних? (y/n): ").strip().lower()
        if save in ["y", "yes", "так", "т"]:
            desc = f"{info['ukr_name']} (Аудіоаналіз: {res['status_description']})"
            rec_id = self.db.add_record(
                analysis_type="audio",
                predicted_species=species,
                confidence=res["confidence"],
                description=desc,
                scientific_name=info["scientific_name"],
                family=info["family"],
                habitat=info["habitat"],
                region=info["region"],
                diet=info["diet"],
                audio_name=aud_path.name,
                audio_predicted_species=species,
                audio_confidence=res["confidence"],
                top3_list=res["variants"],
                additional_info=res["status_description"]
            )
            print(f"Запис успішно додано під номером {rec_id}.")

    def _handle_multimodal_analysis(self) -> None:
        self._print_header("Мультимодальний аналіз (Фото + Аудіо)")
        img_samples = list(config.SAMPLE_DIR.glob("*.jpg"))
        aud_samples = list(config.SAMPLE_DIR.glob("*.wav"))

        if not img_samples or not aud_samples:
            print("Відсутні тестові зразки в папці sample_data.")
            return

        print("Оберіть зразок фотографії:")
        for idx, img in enumerate(img_samples[:6], 1):
            print(f"{idx}. {img.name}")
        img_choice = input("Номер фото: ").strip()
        if not img_choice.isdigit() or not (1 <= int(img_choice) <= len(img_samples[:6])):
            print("Некоректний вибір.")
            return
        img_path = img_samples[int(img_choice) - 1]

        print("\nОберіть зразок аудіофайлу:")
        for idx, aud in enumerate(aud_samples, 1):
            print(f"{idx}. {aud.name}")
        aud_choice = input("Номер аудіо: ").strip()
        if not aud_choice.isdigit() or not (1 <= int(aud_choice) <= len(aud_samples)):
            print("Некоректний вибір.")
            return
        aud_path = aud_samples[int(aud_choice) - 1]

        print("\nВиконується комплексний інференс...")
        img_res = self.image_classifier.classify(img_path)
        aud_res = self.audio_classifier.classify(aud_path)

        comp = compare_modalities(
            img_res["predicted_species"],
            aud_res["predicted_species"],
            img_res["confidence"],
            aud_res["confidence"]
        )

        print("\n" + "-" * 50)
        print(f"1. Результат за фото: {img_res['predicted_species']} ({round(img_res['confidence']*100, 1)}%)")
        print(f"2. Результат за аудіо: {aud_res['predicted_species']} ({round(aud_res['confidence']*100, 1)}%)")
        print(f"Вердикт: {comp['verdict']}")
        print(f"Достовірність: {comp['reliability_note']}")
        print("Примітка: Просте зіставлення назв не гарантує приналежність одній особині.")

        save = input("\nЗберегти мультимодальний аналіз у базу даних? (y/n): ").strip().lower()
        if save in ["y", "yes", "так", "т"]:
            info = self.info_repo.find_bird_info(img_res["predicted_species"])
            rec_id = self.db.add_record(
                analysis_type="multimodal",
                predicted_species=img_res["predicted_species"],
                confidence=img_res["confidence"],
                image_name=img_path.name,
                description=f"{info['ukr_name']} (Мультимодальне зіставлення)",
                scientific_name=info["scientific_name"],
                family=info["family"],
                habitat=info["habitat"],
                region=info["region"],
                diet=info["diet"],
                audio_name=aud_path.name,
                audio_predicted_species=aud_res["predicted_species"],
                audio_confidence=aud_res["confidence"],
                top3_list=img_res["variants"],
                additional_info=f"{comp['verdict']}. {comp['reliability_note']}"
            )
            print(f"Запис успішно додано під номером {rec_id}.")

    def _handle_database_search(self) -> None:
        self._print_header("База даних - Пошук та перегляд")
        query = input("Введіть запит для пошуку (або Enter для показу всіх): ").strip()
        records = self.db.search_by_name(query) if query else self.db.get_all_records()

        if not records:
            print("Записів не знайдено.")
            return

        print(f"\nЗнайдено записів: {len(records)}\n")
        print(f"{'ID':<4} | {'Тип':<10} | {'Вид птаха':<24} | {'Впевн.':<8} | {'Наукова назва':<24} | {'Дата':<19}")
        print("-" * 98)
        for r in records[:25]:
            conf_str = f"{round(float(r['confidence']) * 100, 1)}%"
            spec = r['predicted_species'][:23]
            sci = (r['scientific_name'] or "-")[:23]
            print(f"{r['id']:<4} | {r['analysis_type']:<10} | {spec:<24} | {conf_str:<8} | {sci:<24} | {r['analysis_date']:<19}")

    def _handle_database_filter(self) -> None:
        self._print_header("Фільтрація записів бази даних")
        families = self.info_repo.get_all_families()
        print("Доступні родини:")
        for idx, fam in enumerate(families[:8], 1):
            print(f"{idx}. {fam}")

        fam_choice = input("\nОберіть номер родини (або Enter для пропуску): ").strip()
        selected_family = None
        if fam_choice.isdigit() and 1 <= int(fam_choice) <= len(families[:8]):
            selected_family = families[int(fam_choice) - 1]

        habitat_query = input("Введіть ключове слово середовища (напр. ліс, водойма, озера): ").strip()
        records = self.db.filter_records(family=selected_family, habitat=habitat_query or None)

        if not records:
            print("За вказаними критеріями записів не знайдено.")
            return

        print(f"\nЗнайдено записів після фільтрації: {len(records)}\n")
        for r in records[:15]:
            print(f"ID: {r['id']} | {r['predicted_species']} | Родина: {r['family']} | Середовище: {r['habitat']}")

    def _handle_delete_record(self) -> None:
        self._print_header("Видалення запису з бази даних")
        rec_id_str = input("Введіть ID запису для видалення: ").strip()
        if not rec_id_str.isdigit():
            print("Некоректний числовий ID.")
            return

        rec_id = int(rec_id_str)
        confirm = input(f"Ви впевнені, що хочете видалити запис ID: {rec_id}? (y/n): ").strip().lower()
        if confirm in ["y", "yes", "так", "т"]:
            success = self.db.delete_record(rec_id)
            if success:
                print(f"Запис ID: {rec_id} успішно видалено.")
            else:
                print(f"Запис з ID: {rec_id} не знайдено.")

    def _handle_species_comparison(self) -> None:
        self._print_header("Порівняння двох біологічних видів")
        all_keys = sorted(list(BIRD_KNOWLEDGE_BASE.keys()))
        print("Оберіть два види зі списку:")
        for idx, k in enumerate(all_keys[:12], 1):
            print(f"{idx}. {k}")

        i1 = input("\nНомер першого виду: ").strip()
        i2 = input("Номер другого виду: ").strip()

        if not (i1.isdigit() and i2.isdigit()):
            print("Некоректне введення номерів.")
            return

        n1, n2 = int(i1), int(i2)
        if not (1 <= n1 <= len(all_keys[:12]) and 1 <= n2 <= len(all_keys[:12])):
            print("Номер поза діапазоном.")
            return

        b1_key = all_keys[n1 - 1]
        b2_key = all_keys[n2 - 1]

        info1 = self.info_repo.find_bird_info(b1_key)
        info2 = self.info_repo.find_bird_info(b2_key)
        comp = compare_two_birds(info1, info2)

        print("\n" + "=" * 80)
        print(f"{'Параметр':<25} | {info1['ukr_name']:<25} | {info2['ukr_name']:<25}")
        print("=" * 80)
        for row in comp["comparison_rows"]:
            p = row["parameter"][:24]
            v1 = str(row["bird1_value"])[:24]
            v2 = str(row["bird2_value"])[:24]
            print(f"{p:<25} | {v1:<25} | {v2:<25}")
        print("-" * 80)
        if comp["same_family"]:
            print("Обидва види належать до однієї біологічної родини.")
        else:
            print("Види належать до різних біологічних родин.")

    def _handle_batch_run(self) -> None:
        self._print_header("Пакетний аналіз тестового набору (15+ фото)")
        print("Запуск обробки всіх зразків із папки sample_data...")
        summary = self.batch_runner.run_full_pipeline()
        print("\nПакетну обробку завершено успішно.")
        print(f"Проаналізовано фотографій: {summary['images_analyzed']}")
        print(f"Проаналізовано мультимодальних пар: {summary['multimodal_analyzed']}")
        print(f"Загальна кількість записів у БД: {summary['total_records']}")
        print(f"Файл результатів CSV: {summary['csv_path']}")
        print(f"Файл графіка: {summary['chart_path']}")

    def _handle_export_and_stats(self) -> None:
        self._print_header("Експорт у CSV та статистика")
        records = self.db.get_all_records()
        if not records:
            print("База даних порожня. Спочатку виконайте аналіз або пакетний прогін.")
            return

        csv_path = export_to_csv(records)
        stats = compute_statistics(records)
        chart_path = generate_distribution_chart(records)

        print(f"Файл експортовано: {csv_path}")
        print(f"Графік розподілу збережено: {chart_path}")
        print(f"\nЗагальна кількість проаналізованих записів: {stats['total_analyzed']}")

        print("\nНайчастіші види:")
        for spec, count in stats["most_frequent_species"]:
            print(f"  - {spec}: {count} разів")

        if stats["highest_confidence"]:
            hc = stats["highest_confidence"]
            print(f"\nНайвища впевненість: {hc['predicted_species']} ({round(float(hc['confidence'])*100, 2)}%) [Файл: {hc['image_name']}]")
        if stats["lowest_confidence"]:
            lc = stats["lowest_confidence"]
            print(f"Найнижча впевненість: {lc['predicted_species']} ({round(float(lc['confidence'])*100, 2)}%) [Файл: {lc['image_name']}]")
