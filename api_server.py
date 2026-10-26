import io
import shutil
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import config
from image_classifier import BirdImageClassifier
from audio_classifier import BirdAudioClassifier
from bird_info import BirdInfoRepository
from comparison import compare_modalities, compare_two_birds

app = FastAPI(title="AI Server - Birdly ML Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

image_classifier = BirdImageClassifier()
audio_classifier = BirdAudioClassifier()
info_repo = BirdInfoRepository()

@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "ok", "service": "AIBirdly ML Server"}

@app.post("/predict/image")
async def predict_image(file: UploadFile = File(...)) -> Dict[str, Any]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Файл не надано.")
    suffix = Path(file.filename).suffix.lower()
    if suffix not in [".jpg", ".jpeg", ".png"]:
        raise HTTPException(status_code=400, detail="Непідтримуваний формат зображення.")

    raw_bytes = await file.read()
    try:
        pil_image = Image.open(io.BytesIO(raw_bytes)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Помилка читання зображення: {str(e)}")

    result = image_classifier.classify(pil_image)
    result["file_name"] = file.filename
    if result["success"]:
        info = info_repo.find_bird_info(result["predicted_species"])
        result["bird_info"] = info
    return result

@app.post("/predict/audio")
async def predict_audio(file: UploadFile = File(...)) -> Dict[str, Any]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Аудіофайл не надано.")
    suffix = Path(file.filename).suffix.lower()
    if suffix not in [".wav", ".flac", ".ogg"]:
        raise HTTPException(status_code=400, detail="Непідтримуваний аудіоформат.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = Path(temp_file.name)

    try:
        result = audio_classifier.classify(temp_path)
        result["file_name"] = file.filename
        if result["success"]:
            info = info_repo.find_bird_info(result["predicted_species"])
            result["bird_info"] = info
        return result
    finally:
        if temp_path.exists():
            temp_path.unlink()

@app.post("/compare/modalities")
def compare_modalities_endpoint(
    image_species: str = Form(...),
    audio_species: str = Form(...),
    image_confidence: float = Form(...),
    audio_confidence: float = Form(...)
) -> Dict[str, Any]:
    return compare_modalities(
        image_species,
        audio_species,
        image_confidence,
        audio_confidence
    )

@app.get("/birds")
def get_all_birds() -> Dict[str, Any]:
    return {
        "families": info_repo.get_all_families(),
        "habitats": info_repo.get_all_habitats(),
        "diets": info_repo.get_all_diets(),
        "species": [
            {"key": k, "ukr_name": v.get("ukr_name", k), "scientific_name": v.get("scientific_name", "")}
            for k, v in info_repo._data.items()
        ]
    }

@app.get("/birds/{species_name}")
def get_bird_info(species_name: str) -> Dict[str, Any]:
    return info_repo.find_bird_info(species_name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host="127.0.0.1", port=8001, reload=False)
