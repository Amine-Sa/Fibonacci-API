from logging import debug
from flask import Flask, config
from flask_restful import Api, Resource
from flask_caching import Cache

from fibonacci import *

app = Flask(__name__)
api = Api(app)
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache"})


class Fibonacci(Resource):
    def get(self, my_number):
        return {"data": fibonacci(my_number)}


class Advanced_Fibonacci(Resource):
    @cache.memoize()
    def get(self, my_number):
        return {"data": advanced_fibonacci(my_number, cache)}


api.add_resource(Fibonacci, "/fibonacci/basic/<int:my_number>")
api.add_resource(Advanced_Fibonacci, "/fibonacci/advanced/<int:my_number>")

if __name__ == "__main__":
    app.run(debug=True)
