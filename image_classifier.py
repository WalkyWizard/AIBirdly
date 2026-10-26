from pathlib import Path
from typing import List, Dict, Any, Union
from PIL import Image
from transformers import pipeline
import config

class BirdImageClassifier:
    def __init__(self, model_id: str = config.IMAGE_MODEL_ID):
        self.model_id = model_id
        self._pipe = None

    def _ensure_pipeline(self) -> None:
        if self._pipe is None:
            self._pipe = pipeline(
                "image-classification",
                model=self.model_id
            )

    def classify(self, image_input: Union[str, Path, Image.Image], top_k: int = config.TOP_K_PREDICTIONS) -> Dict[str, Any]:
        self._ensure_pipeline()
        opened_image = None
        file_name = "in_memory"

        try:
            if isinstance(image_input, (str, Path)):
                path = Path(image_input)
                if not path.exists():
                    raise FileNotFoundError(f"Файл не знайдено: {path}")
                if path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
                    raise ValueError("Непідтримуваний формат зображення. Дозволені: JPG, JPEG, PNG.")
                file_name = path.name
                opened_image = Image.open(path).convert("RGB")
            elif isinstance(image_input, Image.Image):
                opened_image = image_input.convert("RGB")
            else:
                raise TypeError("Некоректний тип вхідних даних для зображення.")

            raw_results = self._pipe(opened_image, top_k=top_k)
            formatted_results: List[Dict[str, Any]] = []

            for item in raw_results:
                clean_label = str(item["label"]).strip()
                confidence = float(item["score"])
                formatted_results.append({
                    "species": clean_label,
                    "confidence": round(confidence, 4)
                })

            top_variant = formatted_results[0]
            return {
                "success": True,
                "file_name": file_name,
                "predicted_species": top_variant["species"],
                "confidence": top_variant["confidence"],
                "variants": formatted_results,
                "is_confident": top_variant["confidence"] >= config.CONFIDENCE_THRESHOLD,
                "error": None
            }
        except Exception as e:
            return {
                "success": False,
                "file_name": file_name,
                "predicted_species": "Помилка аналізу",
                "confidence": 0.0,
                "variants": [],
                "is_confident": False,
                "error": str(e)
            }
