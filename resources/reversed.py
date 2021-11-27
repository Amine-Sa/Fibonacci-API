from flask_restful import Resource
from comon.util import reverse_fibonacci


class Reverse_Fibonacci(Resource):
    def get(self, k):
        return {"data": reverse_fibonacci(k)}
