from typing import Dict, Any

def normalize_name(name: str) -> str:
    return name.strip().upper().replace("_", " ").replace("-", " ")

def compare_modalities(
    image_species: str,
    audio_species: str,
    image_conf: float,
    audio_conf: float
) -> Dict[str, Any]:
    norm_img = normalize_name(image_species)
    norm_aud = normalize_name(audio_species)

    is_exact_match = norm_img == norm_aud
    is_partial_match = norm_img in norm_aud or norm_aud in norm_img

    if is_exact_match:
        verdict = "Повний збіг: фото та аудіо визначили однаковий вид птаха"
        match_level = "high"
    elif is_partial_match:
        verdict = "Частковий збіг: назви видів мають спільну основу"
        match_level = "medium"
    else:
        verdict = "Розбіжність: фотографія та аудіозапис належать до різних видів"
        match_level = "none"

    reliability_note = "Обидва аналізи мають високу достовірність"
    if image_conf < 0.5 and audio_conf < 0.5:
        reliability_note = "Обидві моделі мають низький рівень упевненості, результат потребує ручної перевірки"
    elif image_conf < 0.5:
        reliability_note = "Модель розпізнавання фото має низьку впевненість"
    elif audio_conf < 0.5:
        reliability_note = "Модель розпізнавання аудіо має низьку впевненість, результат є гіпотезою"

    return {
        "is_match": is_exact_match or is_partial_match,
        "match_level": match_level,
        "verdict": verdict,
        "reliability_note": reliability_note,
        "image_species": image_species,
        "audio_species": audio_species,
        "image_confidence": image_conf,
        "audio_confidence": audio_conf
    }

def compare_two_birds(bird1: Dict[str, str], bird2: Dict[str, str]) -> Dict[str, Any]:
    fields_to_compare = [
        ("Українська назва", "ukr_name"),
        ("Наукова назва", "scientific_name"),
        ("Родина", "family"),
        ("Середовище існування", "habitat"),
        ("Географічне поширення", "region"),
        ("Тип живлення", "diet"),
        ("Розміри", "size"),
        ("Природоохоронний статус", "conservation_status")
    ]

    comparison_rows = []
    same_family = bird1.get("family") == bird2.get("family") and bird1.get("family") != "Дані відсутні"

    for label, key in fields_to_compare:
        val1 = bird1.get(key, "Дані відсутні")
        val2 = bird2.get(key, "Дані відсутні")
        comparison_rows.append({
            "parameter": label,
            "bird1_value": val1,
            "bird2_value": val2,
            "is_identical": val1 == val2
        })

    return {
        "bird1_name": bird1.get("ukr_name", "Птах 1"),
        "bird2_name": bird2.get("ukr_name", "Птах 2"),
        "same_family": same_family,
        "comparison_rows": comparison_rows
    }
