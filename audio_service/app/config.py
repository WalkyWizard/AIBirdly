import os

AUDIO_MODEL_ID = "dima806/bird_sounds_classification"
TOP_K_PREDICTIONS = 3
CONFIDENCE_THRESHOLD = 0.50
AUDIO_SAMPLE_RATE = 16000
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8002"))
