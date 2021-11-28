from flask import Flask
from flask_restful import Api, Resource

from resources import cache
from resources.basic import Fibonacci
from resources.reversed import Reverse_Fibonacci
from resources.advanced import Advanced_Fibonacci
from resources.funcache import Functools_Fibonacci


app = Flask(__name__)
api = Api(app)
cache.init_app(app)


api.add_resource(Fibonacci, "/v1/fibonacci/basic/<int:my_number>")
api.add_resource(Functools_Fibonacci, "/v1/fibonacci/functools/<int:my_number>")
api.add_resource(Advanced_Fibonacci, "/v1/fibonacci/advanced/<int:my_number>")
api.add_resource(Reverse_Fibonacci, "/v1/reverse-fibonacci/<int:k>")

if __name__ == "__main__":
    app.run(debug=True)
