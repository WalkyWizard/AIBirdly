from pathlib import Path
from typing import List, Dict, Any, Union
import numpy as np
import soundfile as sf
from transformers import pipeline
import config

class BirdAudioClassifier:
    def __init__(self, model_id: str = config.AUDIO_MODEL_ID):
        self.model_id = model_id
        self._pipe = None

    def _ensure_pipeline(self) -> None:
        if self._pipe is None:
            self._pipe = pipeline(
                "audio-classification",
                model=self.model_id
            )

    def classify(self, audio_path: Union[str, Path], top_k: int = config.TOP_K_PREDICTIONS) -> Dict[str, Any]:
        self._ensure_pipeline()
        path = Path(audio_path)

        try:
            if not path.exists():
                raise FileNotFoundError(f"Аудіофайл не знайдено: {path}")

            allowed_extensions = [".wav", ".flac", ".ogg"]
            if path.suffix.lower() not in allowed_extensions:
                raise ValueError(f"Непідтримуваний формат. Дозволені: {', '.join(allowed_extensions)}")

            audio_data, sample_rate = sf.read(str(path))
            if audio_data.ndim > 1:
                audio_data = np.mean(audio_data, axis=1)

            audio_payload = {
                "raw": audio_data.astype(np.float32),
                "sampling_rate": int(sample_rate)
            }

            raw_results = self._pipe(audio_payload, top_k=top_k)
            formatted_results: List[Dict[str, Any]] = []

            for item in raw_results:
                clean_label = str(item["label"]).strip()
                confidence = float(item["score"])
                formatted_results.append({
                    "species": clean_label,
                    "confidence": round(confidence, 4)
                })

            top_variant = formatted_results[0]
            is_reliable = top_variant["confidence"] >= config.CONFIDENCE_THRESHOLD

            status_description = "Підтверджений результат" if is_reliable else "Припущення (низький рівень упевненості)"

            return {
                "success": True,
                "file_name": path.name,
                "predicted_species": top_variant["species"],
                "confidence": top_variant["confidence"],
                "is_reliable": is_reliable,
                "status_description": status_description,
                "variants": formatted_results,
                "error": None
            }
        except Exception as e:
            return {
                "success": False,
                "file_name": path.name if isinstance(path, Path) else "unknown",
                "predicted_species": "Помилка аналізу",
                "confidence": 0.0,
                "is_reliable": False,
                "status_description": "Помилка обробки аудіо",
                "variants": [],
                "error": str(e)
            }
