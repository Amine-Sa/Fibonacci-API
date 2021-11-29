import unittest
import json

from hypothesis import given
from hypothesis.strategies import integers

from app import app
from comon.util import *


class Fib_basic(unittest.TestCase):
    def test_index(self):
        """Testing the respone status code for basic fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/fibonacci/basic/1")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_content_type(self):
        """Testing the content type for basic fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/fibonacci/basic/1")
        self.assertEqual(response.content_type, "application/json")

    def test_content_values(self):
        """Testing the content values for basic fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/fibonacci/basic/1")
        self.assertEqual(json.loads(response.data)["data"], 1)
        response = tester.get("/v1/fibonacci/basic/2")
        self.assertEqual(json.loads(response.data)["data"], 1)
        response = tester.get("/v1/fibonacci/basic/5")
        self.assertEqual(json.loads(response.data)["data"], 5)
        response = tester.get("/v1/fibonacci/basic/7")
        self.assertEqual(json.loads(response.data)["data"], 13)


class Fib_functools(unittest.TestCase):
    def test_index(self):
        """Testing the respone status code for functools fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/fibonacci/functools/1")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_content_type(self):
        """Testing the content type for functools fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/fibonacci/functools/1")
        self.assertEqual(response.content_type, "application/json")

    @given(integers(min_value=0, max_value=20))
    def test_function(self, num):
        """Testing the functools fibonacci functions results"""
        assert functools_fibonacci(num) == fibonacci(num)

class Fib_advanced(unittest.TestCase):
    def test_index(self):
        """Testing the respone status code for advanced fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/fibonacci/advanced/1")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_content_type(self):
        """Testing the content type for advanced fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/fibonacci/advanced/1")
        self.assertEqual(response.content_type, "application/json")

    def test_content_values(self):
        """Testing the content values for advanced fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/fibonacci/advanced/1")
        self.assertEqual(json.loads(response.data)["data"], 1)
        response = tester.get("/v1/fibonacci/advanced/2")
        self.assertEqual(json.loads(response.data)["data"], 1)
        response = tester.get("/v1/fibonacci/advanced/5")
        self.assertEqual(json.loads(response.data)["data"], 5)
        response = tester.get("/v1/fibonacci/advanced/7")
        self.assertEqual(json.loads(response.data)["data"], 13)


class Reverse_Fibo(unittest.TestCase):
    def test_index(self):
        """Testing the respone status code for reverse fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/reverse-fibonacci/2")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_content_type(self):
        """Testing the content type for reverse fibonacci implementation"""
        tester = app.test_client(self)
        response = tester.get("/v1/reverse-fibonacci/2")
        self.assertEqual(response.content_type, "application/json")

    @given(integers(min_value=2, max_value=50))
    def test_function(self, num):
        """Testing the reverse fibonacci functions results"""
        assert reverse_fibonacci(functools_fibonacci(num)) == num


if __name__ == "__main__":
    unittest.main()
