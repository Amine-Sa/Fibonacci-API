from main import app
import unittest
import json


class Fib_basic(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/fibonacci/basic/1")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get("/fibonacci/basic/1")
        self.assertEqual(response.content_type, "application/json")

    def test_content_values(self):
        tester = app.test_client(self)
        response = tester.get("/fibonacci/basic/1")
        self.assertEqual(json.loads(response.data)["data"], 1)
        response = tester.get("/fibonacci/basic/2")
        self.assertEqual(json.loads(response.data)["data"], 1)
        response = tester.get("/fibonacci/basic/5")
        self.assertEqual(json.loads(response.data)["data"], 5)
        response = tester.get("/fibonacci/basic/7")
        self.assertEqual(json.loads(response.data)["data"], 13)


class Fib_advanced(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/fibonacci/advanced/1")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get("/fibonacci/advanced/1")
        self.assertEqual(response.content_type, "application/json")

    def test_content_values(self):
        tester = app.test_client(self)
        response = tester.get("/fibonacci/advanced/1")
        self.assertEqual(json.loads(response.data)["data"], 1)
        response = tester.get("/fibonacci/advanced/2")
        self.assertEqual(json.loads(response.data)["data"], 1)
        response = tester.get("/fibonacci/advanced/5")
        self.assertEqual(json.loads(response.data)["data"], 5)
        response = tester.get("/fibonacci/advanced/7")
        self.assertEqual(json.loads(response.data)["data"], 13)


if __name__ == "__main__":
    unittest.main()
