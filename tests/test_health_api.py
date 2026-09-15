import unittest

from src.health_api import app


class HealthApiTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertEqual(
            response.get_json(),
            {
                "service": "healthcare-ai-data-science",
                "status": "healthy",
            },
        )

    def test_unknown_route(self):
        response = self.client.get("/does-not-exist")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, "application/json")
        self.assertEqual(
            response.get_json(),
            {
                "error": "Resource not found",
                "status": 404,
            },
        )


if __name__ == "__main__":
    unittest.main()