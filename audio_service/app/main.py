import shutil
import tempfile
from pathlib import Path
from typing import Dict, Any
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .audio_classifier import BirdAudioClassifier
from .bird_info import BirdInfoRepository

app = FastAPI(title="Bird Audio Classification Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

classifier = BirdAudioClassifier()
info_repo = BirdInfoRepository()

@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "ok", "service": "Bird Audio Classification Microservice"}

@app.post("/predict/audio")
async def predict_audio(file: UploadFile = File(...)) -> Dict[str, Any]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Аудіофайл не надано")
    suffix = Path(file.filename).suffix.lower()
    if suffix not in [".wav", ".flac", ".ogg", ".mp3", ".m4a", ".aac"]:
        raise HTTPException(status_code=400, detail="Непідтримуваний аудіоформат")

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = Path(temp_file.name)

    try:
        result = classifier.classify(temp_path)
        result["file_name"] = file.filename
        if result.get("success"):
            info = info_repo.find_bird_info(result["predicted_species"])
            result["bird_info"] = info
        return result
    finally:
        if temp_path.exists():
            temp_path.unlink()
