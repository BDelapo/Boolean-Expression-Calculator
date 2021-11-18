from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import numpy as np
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Calculator(Resource):
    def post(self):

        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('term', required=True)  # add args
   

        args = parser.parse_args()  

        # print(np.array(list(list(args.values()))))
        
        # return {'data': args['term']}, 200  


api.add_resource(Calculator, '/calculator')

if __name__ == '__main__':
    app.run()