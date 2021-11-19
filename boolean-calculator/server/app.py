from flask import Flask, jsonify, json
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
import pandas as pd
import math

app = Flask(__name__)
CORS(app)
api = Api(app)

## Class that calculates the truth values of the terms. Accepts POST requests containing Term in json form and accepts GET requests
## for the resulting calculations
class Calculator(Resource):

    rows = 0
    
    @classmethod
    def post(cls):
        parser = reqparse.RequestParser() 
        
        parser.add_argument("term", required=True)  
   
        args = parser.parse_args()  

        terms = json.loads(args["term"].replace("'", "\""))
        cls.calculate(terms)
        # cls.rows = 999
    
    @classmethod
    def get(cls):
        print('Hello\n\n')
        print(str(cls.rows) + ' jjjj')
        if not isinstance(Calculator.rows, int):
            print(Calculator.rows)
            return Calculator.rows

    @classmethod
    def calculate(cls, terms):
        arr_term = np.array(list(terms.values()))
        operators = np.in1d(arr_term, ['+', '-', '*', '/'])
        operands = (operators == False)
        operand_count = np.count_nonzero(operands == True)

        column_size = 2**operand_count
        columns = np.zeros((operand_count, column_size))

        for i in range(operand_count):
            alternations = 2**(i)
            numbered_column = np.arange(0, column_size)
            boolean_column = np.floor((numbered_column/alternations)%2)
            columns[i] = boolean_column

        row_arr = np.transpose(np.flip(columns)) 
        cls.rows = dict(enumerate(row_arr.flatten()))
        # print(Calculator.rows)


api.add_resource(Calculator, '/calculator')

if __name__ == '__main__':
    app.run()