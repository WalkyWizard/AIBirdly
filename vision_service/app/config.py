import os

IMAGE_MODEL_ID = "chriamue/bird-species-classifier"
TOP_K_PREDICTIONS = 3
CONFIDENCE_THRESHOLD = 0.50
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8001"))
