from . import cache
from flask_restful import Resource
from comon.util import advanced_fibonacci


class Advanced_Fibonacci(Resource):
    @cache.memoize()
    def get(self, my_number):
        return {"data": advanced_fibonacci(my_number, cache)}
