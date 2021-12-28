import numpy as np
import pandas as pd
import copy

def get_variable_rows(operand_dict):
    operands  = np.array(list(operand_dict.values()))
    column_size = 2**operands.size
    columns = np.zeros((operands.size, column_size))
    
    indices = []
    for i in range(operands.size):
        alternations = 2**(i)
        numbered_column = np.arange(0, column_size)
        boolean_column = np.floor((numbered_column/alternations)%2)
        columns[i] = boolean_column
        indices.append(2*i)
    
    row_arr = dict(zip(indices, np.flip(columns)))
    return row_arr

def log_intersection(v1, v2):
    return 1 if v1 == 1 and v2 == 1 else 0

def log_union(v1, v2):
    # print(v1, v2)
    return 1 if v1 == 1 or v2 == 1 else 0

def log_negation(v1):
    return 0 if v1 ==1 else 0 
    
   
def calculate(expression):

    expression_list = list(expression.values())
    # print(type(expression_list))
    if not expression_list:
        return
    elif expression_list[-1] not in ['+', '-', '*']:
        operands = dict(enumerate(np.unique(np.array(expression_list)[::2])))    
    else :
        expression_list.pop()
        operands = dict(enumerate(np.unique(np.array(expression_list)[::2])))
    
    var_rows_dict = get_variable_rows(operands)

    int_operators = np.where(np.array(expression_list) == '*')[0].astype(int)
    union_operators = np.where(np.array(expression_list) == '+')[0].astype(int)
    # print(var_rows_dict)
    # print(len(expression_list))

    exp_value = None
    exp_value_arr = []
    answer_arr = []
    if len(expression_list) > 1:
        for index in range(len(var_rows_dict[0])):
            row_temp = copy.deepcopy(var_rows_dict)
            exp_value_arr.append([])
            for intersection in int_operators:
                exp_value = log_intersection(row_temp[intersection-1][index], row_temp[intersection+1][index])
                row_temp[intersection-1][index] = row_temp[intersection+1][index] = exp_value
                print(' and  ' + str(exp_value))
            exp_value_arr[index].append(exp_value)
            exp_value = None
            for union in union_operators:
                exp_value = log_union(row_temp[union-1][index], row_temp[union+1][index])
                print(' or  ' + str(exp_value))
            exp_value_arr[index].append(exp_value)
            exp_value = None

            print('--------------------------------')

        print(exp_value_arr)

        for row in range(len(var_rows_dict[0])):
            if not union_operators:
                answer_arr.append(0) if 0 in exp_value_arr[row] else answer_arr.append(1)
            else:
                answer_arr.append(1) if 1 in exp_value_arr[row] else answer_arr.append(0)

            var_rows_dict['answer'] = answer_arr
        print(var_rows_dict)

    var_rows = var_rows_dict.values()
    calculations = pd.DataFrame(var_rows)

    return calculations.to_dict()