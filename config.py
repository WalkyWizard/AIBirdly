from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "birds.db"
CSV_EXPORT_PATH = BASE_DIR / "bird_analysis.csv"
SAMPLE_DIR = BASE_DIR / "sample_data"
STATS_PLOT_PATH = BASE_DIR / "classification_stats.png"

IMAGE_MODEL_ID = "chriamue/bird-species-classifier"
AUDIO_MODEL_ID = "dima806/bird_sounds_classification"

TOP_K_PREDICTIONS = 3
CONFIDENCE_THRESHOLD = 0.50
AUDIO_SAMPLE_RATE = 16000

AI_VISION_HOST = "127.0.0.1"
AI_VISION_PORT = 8001
AI_AUDIO_HOST = "127.0.0.1"
AI_AUDIO_PORT = 8002
AI_INFO_HOST = "127.0.0.1"
AI_INFO_PORT = 8003
