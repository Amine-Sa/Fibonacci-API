from flask_restful import Resource
from comon.util import fibonacci


class Fibonacci(Resource):
    def get(self, my_number):
        return {"data": fibonacci(my_number)}