from os import umask
from flask_restful import Resource
from comon.util import functools_fibonacci


class Functools_Fibonacci(Resource):
    def get(self, my_number):
        return {"data": functools_fibonacci(my_number)}
