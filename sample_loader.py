import io
import urllib.request
from pathlib import Path
import numpy as np
import soundfile as sf
from PIL import Image
import config

SAMPLE_PHOTO_SOURCES = [
    ("bird_01_parrot.jpg", "https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=500&q=80"),
    ("bird_02_eagle.jpg", "https://images.unsplash.com/photo-1444464666168-49d633b86797?w=500&q=80"),
    ("bird_03_duck.jpg", "https://images.unsplash.com/photo-1516233758813-a38d024919c5?w=500&q=80"),
    ("bird_04_owl.jpg", "https://images.unsplash.com/photo-1579202673506-ca3ce28943ef?w=500&q=80"),
    ("bird_05_sparrow.jpg", "https://images.unsplash.com/photo-1555169062-013468b47731?w=500&q=80"),
    ("bird_06_flamingo.jpg", "https://images.unsplash.com/photo-1549608276-5786777e6587?w=500&q=80"),
    ("bird_07_kingfisher.jpg", "https://images.unsplash.com/photo-1456926631375-92c8ce872def?w=500&q=80"),
    ("bird_08_puffin.jpg", "https://images.unsplash.com/photo-1506220926022-cc5c12acdb35?w=500&q=80"),
    ("bird_09_toucan.jpg", "https://images.unsplash.com/photo-1544979590-37e9b47eb705?w=500&q=80"),
    ("bird_10_pelican.jpg", "https://images.unsplash.com/photo-1549488344-cbb6c34cf08b?w=500&q=80"),
    ("bird_11_robin.jpg", "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?w=500&q=80"),
    ("bird_12_falcon.jpg", "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&q=80"),
    ("bird_13_hummingbird.jpg", "https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=500&q=80"),
    ("bird_14_woodpecker.jpg", "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=500&q=80"),
    ("bird_15_swan.jpg", "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=500&q=80"),
    ("bird_16_crow.jpg", "https://images.unsplash.com/photo-1517423568366-8b83523034fd?w=500&q=80")
]

def ensure_sample_audio(target_dir: Path) -> list[Path]:
    target_dir.mkdir(parents=True, exist_ok=True)
    audio_paths = []

    file1 = target_dir / "sample_chachalaca_call.wav"
    t1 = np.linspace(0, 3.5, 16000 * 3)
    pulse = np.sin(2 * np.pi * 3 * t1) > 0
    carrier = np.sin(2 * np.pi * 1800 * t1 + 0.3 * np.sin(2 * np.pi * 12 * t1))
    audio1 = (0.4 * carrier * pulse).astype(np.float32)
    sf.write(str(file1), audio1, 16000)
    audio_paths.append(file1)

    file2 = target_dir / "sample_tinamou_whistle.wav"
    t2 = np.linspace(0, 4.0, 16000 * 4)
    f2 = 2400 + 400 * np.sin(2 * np.pi * 1.5 * t2)
    phase = 2 * np.pi * np.cumsum(f2) / 16000
    env = np.exp(-0.8 * ((t2 % 1.0) - 0.5) ** 2)
    audio2 = (0.35 * np.sin(phase) * env).astype(np.float32)
    sf.write(str(file2), audio2, 16000)
    audio_paths.append(file2)

    return audio_paths

def ensure_sample_images(target_dir: Path) -> list[Path]:
    target_dir.mkdir(parents=True, exist_ok=True)
    downloaded_paths = []

    for filename, url in SAMPLE_PHOTO_SOURCES:
        file_path = target_dir / filename
        if not file_path.exists() or file_path.stat().st_size < 5000:
            try:
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                )
                with urllib.request.urlopen(req, timeout=15) as resp:
                    raw_data = resp.read()
                img = Image.open(io.BytesIO(raw_data)).convert("RGB")
                img.thumbnail((500, 500))
                img.save(file_path, "JPEG", quality=85)
                downloaded_paths.append(file_path)
            except Exception:
                fallback_img = Image.new("RGB", (300, 300), color=(160, 190, 220))
                fallback_img.save(file_path, "JPEG")
                downloaded_paths.append(file_path)
        else:
            downloaded_paths.append(file_path)

    return downloaded_paths

def prepare_all_samples() -> dict[str, list[Path]]:
    target = config.SAMPLE_DIR
    images = ensure_sample_images(target)
    audios = ensure_sample_audio(target)
    return {
        "images": images,
        "audios": audios
    }

if __name__ == "__main__":
    res = prepare_all_samples()
    print(f"Prepared {len(res['images'])} images and {len(res['audios'])} audio samples.")
