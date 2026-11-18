import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from audio_service.app.main import app
from audio_service.app.audio_classifier import BirdAudioClassifier


class TestAudioService(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["service"], "Bird Audio Classification Microservice")

    @patch("audio_service.app.main.classifier.classify")
    def test_predict_audio_success(self, mock_classify):
        mock_classify.return_value = {
            "success": True,
            "predicted_species": "MALLARD",
            "confidence": 0.88,
            "variants": [{"species": "MALLARD", "confidence": 0.88}],
            "is_reliable": True,
            "status_description": "Високий рівень упевненості",
            "error": None
        }

        fake_audio_bytes = b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xac\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00"
        response = self.client.post(
            "/predict/audio",
            files={"file": ("bird.wav", fake_audio_bytes, "audio/wav")}
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["predicted_species"], "MALLARD")
        self.assertEqual(data["confidence"], 0.88)
        self.assertIn("bird_info", data)
        self.assertEqual(data["bird_info"]["ukr_name"], "Крижень звичайний")

    def test_predict_audio_unsupported_format(self):
        response = self.client.post(
            "/predict/audio",
            files={"file": ("sound.txt", b"audio test", "text/plain")}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "Непідтримуваний аудіоформат")

    @patch("audio_service.app.main.classifier.classify")
    def test_predict_audio_failure(self, mock_classify):
        mock_classify.return_value = {
            "success": False,
            "file_name": "corrupt.wav",
            "predicted_species": "None",
            "confidence": 0.0,
            "variants": [],
            "is_reliable": False,
            "status_description": "Помилка розпізнавання",
            "error": "Cannot decode audio"
        }

        fake_audio_bytes = b"fake-audio-stream"
        response = self.client.post(
            "/predict/audio",
            files={"file": ("corrupt.wav", fake_audio_bytes, "audio/wav")}
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["success"])
        self.assertNotIn("bird_info", data)

    def test_classifier_unit_file_not_found(self):
        classifier = BirdAudioClassifier()
        classifier._ensure_pipeline = MagicMock()
        res = classifier.classify("missing_bird_song.wav")
        self.assertFalse(res["success"])
        self.assertIn("Аудіофайл не знайдено", res["error"])

    @patch("pathlib.Path.exists", return_value=True)
    def test_classifier_unit_invalid_format(self, mock_exists):
        classifier = BirdAudioClassifier()
        classifier._ensure_pipeline = MagicMock()
        res = classifier.classify("invalid_sound.exe")
        self.assertFalse(res["success"])
        self.assertIn("Непідтримуваний формат", res["error"])


if __name__ == "__main__":
    unittest.main()