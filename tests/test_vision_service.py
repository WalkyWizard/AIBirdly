import io
import unittest
from unittest.mock import patch, MagicMock
from PIL import Image
from fastapi.testclient import TestClient
from vision_service.app.main import app
from vision_service.app.image_classifier import BirdImageClassifier
from vision_service.app.bird_info import BirdInfoRepository


class TestVisionService(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["service"], "Bird Vision Classification Microservice")

    @patch("vision_service.app.main.classifier.classify")
    def test_predict_image_success(self, mock_classify):
        mock_classify.return_value = {
            "success": True,
            "is_bird": True,
            "predicted_species": "MALLARD",
            "confidence": 0.95,
            "variants": [{"species": "MALLARD", "confidence": 0.95}],
            "is_confident": True,
            "error": None
        }

        img_byte_arr = io.BytesIO()
        image = Image.new("RGB", (30, 30), color="blue")
        image.save(img_byte_arr, format="PNG")
        img_bytes = img_byte_arr.getvalue()

        response = self.client.post(
            "/predict/image",
            files={"file": ("bird.png", img_bytes, "image/png")}
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["predicted_species"], "MALLARD")
        self.assertAlmostEqual(data["confidence"], 0.95)
        self.assertIn("bird_info", data)
        self.assertEqual(data["bird_info"]["ukr_name"], "Крижень звичайний")

    @patch("vision_service.app.main.classifier.classify")
    def test_predict_image_non_bird(self, mock_classify):
        mock_classify.return_value = {
            "success": True,
            "is_bird": False,
            "predicted_species": "Нічого не знайдено",
            "confidence": 0.0,
            "variants": [],
            "is_confident": False,
            "error": None
        }

        img_byte_arr = io.BytesIO()
        image = Image.new("RGB", (30, 30), color="blue")
        image.save(img_byte_arr, format="PNG")

        response = self.client.post(
            "/predict/image",
            files={"file": ("face.png", img_byte_arr.getvalue(), "image/png")}
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["predicted_species"], "Нічого не знайдено")
        self.assertIsNone(data["bird_info"])

    def test_predict_image_unsupported_format(self):
        response = self.client.post(
            "/predict/image",
            files={"file": ("bird.txt", b"not an image", "text/plain")}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "Непідтримуваний формат зображення")

    def test_predict_image_corrupted_image(self):
        response = self.client.post(
            "/predict/image",
            files={"file": ("corrupted.png", b"corrupted bytes", "image/png")}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Помилка читання зображення", response.json()["detail"])

    @patch("vision_service.app.main.classifier.classify")
    def test_predict_image_classifier_failure(self, mock_classify):
        mock_classify.return_value = {
            "success": False,
            "file_name": "bird.png",
            "predicted_species": "None",
            "confidence": 0.0,
            "variants": [],
            "is_confident": False,
            "error": "Pipeline error"
        }

        img_byte_arr = io.BytesIO()
        image = Image.new("RGB", (10, 10), color="red")
        image.save(img_byte_arr, format="PNG")

        response = self.client.post(
            "/predict/image",
            files={"file": ("bird.png", img_byte_arr.getvalue(), "image/png")}
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["success"])
        self.assertNotIn("bird_info", data)

    def test_classifier_unit_file_not_found(self):
        classifier = BirdImageClassifier()
        classifier._ensure_pipeline = MagicMock()
        res = classifier.classify("non_existent_file_path.jpg")
        self.assertFalse(res["success"])
        self.assertIn("Файл не знайдено", res["error"])

    def test_classifier_unit_invalid_format(self):
        classifier = BirdImageClassifier()
        classifier._ensure_pipeline = MagicMock()
        res = classifier.classify("invalid.txt")
        self.assertFalse(res["success"])

    def test_bird_info_repo_found(self):
        repo = BirdInfoRepository()
        info = repo.find_bird_info("MALLARD")
        self.assertEqual(info["ukr_name"], "Крижень звичайний")
        self.assertEqual(info["scientific_name"], "Anas platyrhynchos")

    def test_bird_info_repo_not_found(self):
        repo = BirdInfoRepository()
        info = repo.find_bird_info("NON_EXISTENT_BIRD_XYZ")
        self.assertEqual(info["ukr_name"], "Немає в довіднику (дані відсутні)")


if __name__ == "__main__":
    unittest.main()