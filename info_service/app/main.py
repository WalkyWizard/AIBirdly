from typing import Dict, Any
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from .bird_info import BirdInfoRepository
from .comparison import compare_modalities, compare_two_birds

app = FastAPI(title="Bird Taxonomy and Comparison Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

info_repo = BirdInfoRepository()

@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "ok", "service": "Bird Taxonomy and Comparison Microservice"}

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

@app.post("/compare/species")
def compare_species_endpoint(
    species_a: str = Form(...),
    species_b: str = Form(...)
) -> Dict[str, Any]:
    b1 = info_repo.find_bird_info(species_a)
    b2 = info_repo.find_bird_info(species_b)
    return compare_two_birds(b1, b2)
