import sys
from pathlib import Path
import config
from sample_loader import prepare_all_samples

def main():
    if not config.SAMPLE_DIR.exists() or not list(config.SAMPLE_DIR.glob("*.jpg")):
        prepare_all_samples()

    if len(sys.argv) > 1 and sys.argv[1] in ["--batch", "--test"]:
        from batch_runner import BatchRunner
        runner = BatchRunner()
        summary = runner.run_full_pipeline()
        print("Пакетний аналіз успішно завершено.")
        print(f"Кількість записів у базі даних: {summary['total_records']}")
        print(f"CSV збережено у: {summary['csv_path']}")
        print(f"Графік збережено у: {summary['chart_path']}")
        print(f"Найчастіші види: {summary['stats']['most_frequent_species']}")
        return

    from cli import BirdLabCLI
    app = BirdLabCLI()
    app.run()

if __name__ == "__main__":
    main()
