from flask import Flask, jsonify, json
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)
api = Api(app)

class Calculator(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument("term", required=True)  # add args
   
        args = parser.parse_args()  

        print(args)
        # terms = json.loads(args["term"].replace("'", "\""))
        # print(terms)
        # self.calculate(terms)


    def calculate(self, terms):
        for values in terms.values():
            print(values)

api.add_resource(Calculator, '/calculator')

if __name__ == '__main__':
    app.run()