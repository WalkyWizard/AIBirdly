import unittest
from fastapi.testclient import TestClient
from info_service.app.main import app
from info_service.app.comparison import compare_modalities, compare_two_birds


class TestInfoService(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["service"], "Bird Taxonomy and Comparison Microservice")

    def test_get_all_birds(self):
        response = self.client.get("/birds")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("families", data)
        self.assertIn("habitats", data)
        self.assertIn("diets", data)
        self.assertIn("species", data)
        self.assertIsInstance(data["families"], list)
        self.assertGreater(len(data["species"]), 0)

    def test_get_bird_info_known(self):
        response = self.client.get("/birds/MALLARD")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["ukr_name"], "Крижень звичайний")
        self.assertEqual(data["scientific_name"], "Anas platyrhynchos")

    def test_get_bird_info_unknown(self):
        response = self.client.get("/birds/NON_EXISTENT_BIRD")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["ukr_name"], "Немає в довіднику (дані відсутні)")

    def test_compare_modalities_match(self):
        response = self.client.post(
            "/compare/modalities",
            data={
                "image_species": "MALLARD",
                "audio_species": "MALLARD",
                "image_confidence": "0.95",
                "audio_confidence": "0.91"
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["is_match"])
        self.assertEqual(data["match_level"], "high")
        self.assertIn("Повний збіг", data["verdict"])

    def test_compare_modalities_mismatch(self):
        response = self.client.post(
            "/compare/modalities",
            data={
                "image_species": "MALLARD",
                "audio_species": "BARN OWL",
                "image_confidence": "0.9",
                "audio_confidence": "0.8"
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["is_match"])
        self.assertEqual(data["match_level"], "none")
        self.assertIn("Розбіжність", data["verdict"])

    def test_compare_modalities_low_confidence(self):
        response = self.client.post(
            "/compare/modalities",
            data={
                "image_species": "MALLARD",
                "audio_species": "BARN OWL",
                "image_confidence": "0.3",
                "audio_confidence": "0.4"
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("Обидві моделі мають низький рівень упевненості", data["reliability_note"])

    def test_compare_species_endpoint(self):
        response = self.client.post(
            "/compare/species",
            data={
                "species_a": "MALLARD",
                "species_b": "BALD EAGLE"
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("comparison_rows", data)
        self.assertFalse(data["same_family"])
        self.assertEqual(data["bird1_name"], "Крижень звичайний")
        self.assertEqual(data["bird2_name"], "Орлан білоголовий")

    def test_compare_two_birds_same_family(self):
        b1 = {"ukr_name": "Птах 1", "family": "Качкові (Anatidae)"}
        b2 = {"ukr_name": "Птах 2", "family": "Качкові (Anatidae)"}
        res = compare_two_birds(b1, b2)
        self.assertTrue(res["same_family"])
        self.assertEqual(len(res["comparison_rows"]), 8)


if __name__ == "__main__":
    unittest.main()