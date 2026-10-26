from pathlib import Path
from typing import Dict, Any, List
import config
from database import BirdDatabase
from bird_info import BirdInfoRepository
from image_classifier import BirdImageClassifier
from audio_classifier import BirdAudioClassifier
from comparison import compare_modalities
from exporter import export_to_csv, compute_statistics, generate_distribution_chart

class BatchRunner:
    def __init__(self):
        self.db = BirdDatabase(config.DATABASE_PATH)
        self.info_repo = BirdInfoRepository()
        self.image_classifier = BirdImageClassifier()
        self.audio_classifier = BirdAudioClassifier()

    def run_image_batch(self, image_paths: List[Path]) -> List[Dict[str, Any]]:
        results = []
        for img_path in image_paths:
            analysis = self.image_classifier.classify(img_path, top_k=config.TOP_K_PREDICTIONS)
            if not analysis["success"]:
                continue

            species = analysis["predicted_species"]
            conf = analysis["confidence"]
            variants = analysis["variants"]
            info = self.info_repo.find_bird_info(species)

            desc = f"{info['ukr_name']} ({info['scientific_name']})"
            add_info = f"Середовище: {info['habitat']}. Родина: {info['family']}. Живлення: {info['diet']}."

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
                top3_list=variants,
                additional_info=add_info
            )
            analysis["record_id"] = rec_id
            analysis["info"] = info
            results.append(analysis)
        return results

    def run_multimodal_batch(self, pairs: List[tuple[Path, Path]]) -> List[Dict[str, Any]]:
        results = []
        for img_path, aud_path in pairs:
            img_res = self.image_classifier.classify(img_path)
            aud_res = self.audio_classifier.classify(aud_path)

            if not img_res["success"] or not aud_res["success"]:
                continue

            comp = compare_modalities(
                img_res["predicted_species"],
                aud_res["predicted_species"],
                img_res["confidence"],
                aud_res["confidence"]
            )

            info = self.info_repo.find_bird_info(img_res["predicted_species"])
            desc = f"{info['ukr_name']} (Порівняння: {comp['verdict']})"
            add_info = f"{comp['verdict']}. {comp['reliability_note']}"

            rec_id = self.db.add_record(
                analysis_type="multimodal",
                predicted_species=img_res["predicted_species"],
                confidence=img_res["confidence"],
                image_name=img_path.name,
                description=desc,
                scientific_name=info["scientific_name"],
                family=info["family"],
                habitat=info["habitat"],
                region=info["region"],
                diet=info["diet"],
                audio_name=aud_path.name,
                audio_predicted_species=aud_res["predicted_species"],
                audio_confidence=aud_res["confidence"],
                top3_list=img_res["variants"],
                additional_info=add_info
            )
            results.append({
                "record_id": rec_id,
                "image_result": img_res,
                "audio_result": aud_res,
                "comparison": comp
            })
        return results

    def run_full_pipeline(self) -> Dict[str, Any]:
        image_files = sorted(list(config.SAMPLE_DIR.glob("*.jpg")))
        audio_files = sorted(list(config.SAMPLE_DIR.glob("*.wav")))

        img_results = self.run_image_batch(image_files)

        multimodal_results = []
        if len(image_files) >= 2 and len(audio_files) >= 2:
            pairs = [
                (image_files[0], audio_files[0]),
                (image_files[1], audio_files[1])
            ]
            multimodal_results = self.run_multimodal_batch(pairs)

        all_records = self.db.get_all_records()
        csv_file = export_to_csv(all_records)
        stats = compute_statistics(all_records)
        chart_file = generate_distribution_chart(all_records)

        return {
            "images_analyzed": len(img_results),
            "multimodal_analyzed": len(multimodal_results),
            "total_records": len(all_records),
            "csv_path": str(csv_file),
            "chart_path": str(chart_file),
            "stats": stats
        }

if __name__ == "__main__":
    runner = BatchRunner()
    summary = runner.run_full_pipeline()
    print("Batch processing completed successfully.")
    print(f"Total records in DB: {summary['total_records']}")
    print(f"CSV exported to: {summary['csv_path']}")
    print(f"Chart saved to: {summary['chart_path']}")
    print(f"Most frequent species: {summary['stats']['most_frequent_species']}")
    if summary['stats']['highest_confidence']:
        print(f"Highest confidence: {summary['stats']['highest_confidence']['predicted_species']} ({summary['stats']['highest_confidence']['confidence']})")
    if summary['stats']['lowest_confidence']:
        print(f"Lowest confidence: {summary['stats']['lowest_confidence']['predicted_species']} ({summary['stats']['lowest_confidence']['confidence']})")
