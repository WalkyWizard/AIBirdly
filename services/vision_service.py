import io
from pathlib import Path
from typing import Dict, Any
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import config
from image_classifier import BirdImageClassifier
from bird_info import BirdInfoRepository

app = FastAPI(title="Bird Vision Classification Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

classifier = BirdImageClassifier()
info_repo = BirdInfoRepository()

@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "ok", "service": "Bird Vision Classification Microservice"}

@app.post("/predict/image")
async def predict_image(file: UploadFile = File(...)) -> Dict[str, Any]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Файл не надано")
    suffix = Path(file.filename).suffix.lower()
    if suffix not in [".jpg", ".jpeg", ".png"]:
        raise HTTPException(status_code=400, detail="Непідтримуваний формат зображення")

    raw_bytes = await file.read()
    try:
        pil_image = Image.open(io.BytesIO(raw_bytes)).convert("RGB")
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Помилка читання зображення: {str(exc)}")

    result = classifier.classify(pil_image)
    result["file_name"] = file.filename
    if result.get("success"):
        info = info_repo.find_bird_info(result["predicted_species"])
        result["bird_info"] = info
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("services.vision_service:app", host=config.AI_VISION_HOST, port=config.AI_VISION_PORT, reload=False)
