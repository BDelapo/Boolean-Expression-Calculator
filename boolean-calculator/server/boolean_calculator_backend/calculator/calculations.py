# import numpy as np
# import pandas as pd
# import copy


import numpy as np
import pandas as pd
import copy

# # def get_variable_rows(operand_dict):
# #     operands  = np.array(list(operand_dict.values()))
# #     column_size = 2**operands.size
# #     columns = np.zeros((operands.size, column_size))
    
# #     indices = []
# #     for i in range(operands.size):
# #         alternations = 2**(i)
# #         numbered_column = np.arange(0, column_size)
# #         boolean_column = np.floor((numbered_column/alternations)%2)
# #         columns[i] = boolean_column
# #         indices.append(2*i)
    
# #     row_arr = dict(zip(indices, np.flip(columns)))
# #     return row_arr

# # def log_intersection(v1, v2):
# #     return 1 if v1 == 1 and v2 == 1 else 0

# # def log_union(v1, v2):
# #     # print(v1, v2)
# #     return 1 if v1 == 1 or v2 == 1 else 0

# # def log_negation(v1):
# #     return 0 if v1 ==1 else 0 
    
# ### TODO Make search tree   
class Node():
    
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class exp_tree():
    
    def __init__(self, exp):
        self.exp = exp = self.parse_exp(exp)
        self.tree_root = self.create_tree(self.exp)
    
    def create_tree(self, exp):
        left = exp[0] if type(exp[0]) != list else self.create_tree(exp[0])
        right = exp[1] if type(exp[1]) != list else self.create_tree(exp[1])
        val = exp[2]
        node = Node(val, left, right)
        return node
            
    def parse_exp(self, exp):
        new_exp = copy.deepcopy(exp)
        sub_exp = []
        start = None
        index = None
        count = 0
        for i in range(len(exp)):
            item = exp[i]
            
            if item != ')' or item != '(':
                sub_exp.append(item)
                    
            if item == '(' :
                count += 1
                if not start:
                    start = True
                    index = i+1
                
            if item == ')':
                if count != 0:
                    count -= 1
                if count == 0:
                    sub_exp.append(self.parse_exp(new_exp[index:i]))
                    del sub_exp[index-1: i+1]

        sub_exp = self.postfix(sub_exp)
        return sub_exp[0]
    
    def postfix(self, exp):
        operators = ['-', '*', '+']
        for o in operators:
            length = len(exp)
            i = 0
            
            if o == '-':
                while i < length:
                    if exp[i] == o:
                        term = [exp[i+1], exp[i]]
                        exp.insert(i+2, term)
                        del exp[i:i+2]
                        length -= 1
                    else:    
                        i += 1  
            else:         
                while i < length:
                    if exp[i] == o:
                        term = [exp[i-1], exp[i+1], exp[i]]
                        exp.insert(i+2, term)
                        del exp[i-1:i+2]
                        length -= 2
                    else:    
                        i += 1
        return exp
            
    def evaluate_tree(self, var_val, tree='root'): 
        
        if tree == 'root':
            tree = self.tree_root
            
        val = tree.val
        if type(tree.left) != Node:
            left = var_val[tree.left]
        else: 
            left = self.evaluate_tree(var_val, tree.left)
            
        if type(tree.right) != Node:
            right = var_val[tree.right]
        else:
            right = self.evaluate_tree(var_val, tree.right)
            
        if val == '*':
            result = self.log_intersection(left, right)
            
        if val == '+':
            result = self.log_union(left, right)

        
        return result
        
    def log_intersection(self, v1, v2):
        return 1 if v1 == 1 and v2 == 1 else 0

    def log_union(self, v1, v2):
        return 1 if v1 == 1 or v2 == 1 else 0

    def log_negation(self, v1):
        return 0 if v1 ==1 else 0

    
def get_variable_rows(operand_dict):
    operands  = np.array(list(operand_dict.values()))
#     print(operands)
    column_size = 2**operands.size
    columns = np.zeros((operands.size, column_size))
    
    indices = []
    for i in range(operands.size):
#         print(i)
        alternations = 2**(i)
        numbered_column = np.arange(0, column_size)
        boolean_column = np.floor((numbered_column/alternations)%2)
        columns[i] = boolean_column
        indices.append(operands[i])
#         print(indices)

        row_arr = dict(zip(indices, np.flip(columns)))
        row_arr = pd.DataFrame(row_arr).to_dict()
#         print(row_arr)
    return row_arr


def calculate(expression):
    expression_list = list(filter(lambda a: a not in ['+', '-', '*', ')', '('], expression.values()))

    if not expression_list:
        return
    elif expression_list[-1] not in ['+', '-', '*']:
        operands = dict(enumerate(np.unique(np.array(expression_list))))
    else :
        expression_list.pop()
        operands = dict(enumerate(np.unique(np.array(expression_list))))

    var_rows_dict = pd.DataFrame(get_variable_rows(operands))
    
    
    if len(expression) > 2 and expression_list[-1] not in ['+', '-', '*', ')', '(']:
        expression_tree = exp_tree(list(expression.values())) 
        evaluated = []
    
        for index, row in var_rows_dict.iterrows():
            evaluated.append(expression_tree.evaluate_tree(var_val = dict(row[:])))
    
        var_rows_dict['answer'] = evaluated
    calc = var_rows_dict.transpose().to_dict()
    print(calc)
    return calc

# def get_variable_rows(operand_dict):
#     operands  = np.array(list(operand_dict.values()))
#     column_size = 2**operands.size
#     columns = np.zeros((operands.size, column_size))
    
#     indices = []
#     for i in range(operands.size):
#         alternations = 2**(i)
#         numbered_column = np.arange(0, column_size)
#         boolean_column = np.floor((numbered_column/alternations)%2)
#         columns[i] = boolean_column
#         indices.append(2*i)
    
#     row_arr = dict(zip(indices, np.flip(columns)))
#     return row_arr

# # def log_intersection(v1, v2):
# #     return 1 if v1 == 1 and v2 == 1 else 0

# # def log_union(v1, v2):
# #     # print(v1, v2)
# #     return 1 if v1 == 1 or v2 == 1 else 0

# # def log_negation(v1):
# #     return 0 if v1 ==1 else 0 
    
# ### TODO Make search tree   
# class Node():
    
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right

# class exp_tree():
    
#     def __init__(self, exp):
#         self.exp = exp = self.parse_exp(exp)
#         self.tree_root = self.create_tree(self.exp)
    
#     def create_tree(self, exp):
#         left = exp[0] if type(exp[0]) != list else self.create_tree(exp[0])
#         right = exp[1] if type(exp[1]) != list else self.create_tree(exp[1])
#         val = exp[2]
#         node = Node(val, left, right)
#         return node
            
#     def parse_exp(self, exp):
#         new_exp = copy.deepcopy(exp)
#         sub_exp = []
#         start = None
#         index = None
#         count = 0
#         for i in range(len(exp)):
#             item = exp[i]
            
#             if item != ')' or item != '(':
#                 sub_exp.append(item)
                    
#             if item == '(' :
#                 count += 1
#                 if not start:
#                     start = True
#                     index = i+1
                
#             if item == ')':
#                 if count != 0:
#                     count -= 1
#                 if count == 0:
#                     sub_exp.append(self.parse_exp(new_exp[index:i]))
#                     del sub_exp[index-1: i+1]

#         sub_exp = self.postfix(sub_exp)
#         return sub_exp[0]
    
#     def postfix(self, exp):
#         operators = ['-', '*', '+']
#         for o in operators:
#             length = len(exp)
#             i = 0
            
#             if o == '-':
#                 while i < length:
#                     if exp[i] == o:
#                         term = [exp[i+1], exp[i]]
#                         exp.insert(i+2, term)
#                         del exp[i:i+2]
#                         length -= 1
#                     else:    
#                         i += 1  
#             else:         
#                 while i < length:
#                     if exp[i] == o:
#                         term = [exp[i-1], exp[i+1], exp[i]]
#                         exp.insert(i+2, term)
#                         del exp[i-1:i+2]
#                         length -= 2
#                     else:    
#                         i += 1
#         return exp
            
#     def evaluate_tree(self, var_val, tree='root'): 
        
#         if tree == 'root':
#             tree = self.tree_root
            
#         val = tree.val
#         if type(tree.left) != Node:
#             left = var_val[tree.left]
#         else: 
#             left = self.evaluate_tree(var_val, tree.left)
            
#         if type(tree.right) != Node:
#             right = var_val[tree.right]
#         else:
#             right = self.evaluate_tree(var_val, tree.right)
            
#         if val == '*':
#             result = self.log_intersection(left, right)
            
#         if val == '+':
#             result = self.log_union(left, right)
# #             print(result)
# #         print(tree.left, tree.right)
#         print(left, val, right)
        
#         return result
        
        
#     def log_intersection(self, v1, v2):
#         return 1 if v1 == 1 and v2 == 1 else 0

#     def log_union(self, v1, v2):
#         return 1 if v1 == 1 or v2 == 1 else 0

#     def log_negation(self, v1):
#         return 0 if v1 ==1 else 0

#     def get_variable_rows(operand_dict):
#         operands  = np.array(list(operand_dict.values()))
#         column_size = 2**operands.size
#         columns = np.zeros((operands.size, column_size))
        
#         indices = []
#         for i in range(operands.size):
#             alternations = 2**(i)
#             numbered_column = np.arange(0, column_size)
#             boolean_column = np.floor((numbered_column/alternations)%2)
#             columns[i] = boolean_column
#             indices.append(2*i)
    
#             row_arr = dict(zip(indices, np.flip(columns)))
#         return row_arr


#     def calculate(expression):

#         expression_list = list(expression.values())
#         # print(type(expression_list))
#         if not expression_list:
#             return
#         elif expression_list[-1] not in ['+', '-', '*']:
#             operands = dict(enumerate(np.unique(np.array(expression_list)[::2])))    
#         else :
#             expression_list.pop()
#             operands = dict(enumerate(np.unique(np.array(expression_list)[::2])))

#         var_rows_dict = get_variable_rows(operands)

#     # int_operators = np.where(np.array(expression_list) == '*')[0].astype(int)
#     # union_operators = np.where(np.array(expression_list) == '+')[0].astype(int)
#     # # print(var_rows_dict)
#     # # print(len(expression_list))

#     # exp_value = None
#     # exp_value_arr = []
#     # answer_arr = []
#     # if len(expression_list) > 1:
#     #     for index in range(len(var_rows_dict[0])):
#     #         row_temp = copy.deepcopy(var_rows_dict)
#     #         exp_value_arr.append([])
#     #         for intersection in int_operators:
#     #             exp_value = log_intersection(row_temp[intersection-1][index], row_temp[intersection+1][index])
#     #             row_temp[intersection-1][index] = row_temp[intersection+1][index] = exp_value
#     #             print(' and  ' + str(exp_value))
#     #         exp_value_arr[index].append(exp_value)
#     #         exp_value = None
#     #         for union in union_operators:
#     #             exp_value = log_union(row_temp[union-1][index], row_temp[union+1][index])
#     #             print(' or  ' + str(exp_value))
#     #         exp_value_arr[index].append(exp_value)
#     #         exp_value = None

#     #         print('--------------------------------')

#     #     print(exp_value_arr)

#     #     for row in range(len(var_rows_dict[0])):
#     #         if not union_operators:
#     #             answer_arr.append(0) if 0 in exp_value_arr[row] else answer_arr.append(1)
#     #         else:
#     #             answer_arr.append(1) if 1 in exp_value_arr[row] else answer_arr.append(0)

#     #         var_rows_dict['answer'] = answer_arr
#     #     print(var_rows_dict)

#         var_rows = var_rows_dict.values()
#         calculations = pd.DataFrame(var_rows)

#         return calculations.to_dict()


# def calculate(expression):

#         expression_list = list(expression.values())
#         # print(type(expression_list))
#         if not expression_list:
#             return
#         elif expression_list[-1] not in ['+', '-', '*']:
#             operands = dict(enumerate(np.unique(np.array(expression_list)[::2])))    
#         else :
#             expression_list.pop()
#             operands = dict(enumerate(np.unique(np.array(expression_list)[::2])))

#         var_rows_dict = get_variable_rows(operands)

#     # int_operators = np.where(np.array(expression_list) == '*')[0].astype(int)
#     # union_operators = np.where(np.array(expression_list) == '+')[0].astype(int)
#     # # print(var_rows_dict)
#     # # print(len(expression_list))

#     # exp_value = None
#     # exp_value_arr = []
#     # answer_arr = []
#     # if len(expression_list) > 1:
#     #     for index in range(len(var_rows_dict[0])):
#     #         row_temp = copy.deepcopy(var_rows_dict)
#     #         exp_value_arr.append([])
#     #         for intersection in int_operators:
#     #             exp_value = log_intersection(row_temp[intersection-1][index], row_temp[intersection+1][index])
#     #             row_temp[intersection-1][index] = row_temp[intersection+1][index] = exp_value
#     #             print(' and  ' + str(exp_value))
#     #         exp_value_arr[index].append(exp_value)
#     #         exp_value = None
#     #         for union in union_operators:
#     #             exp_value = log_union(row_temp[union-1][index], row_temp[union+1][index])
#     #             print(' or  ' + str(exp_value))
#     #         exp_value_arr[index].append(exp_value)
#     #         exp_value = None

#     #         print('--------------------------------')

#     #     print(exp_value_arr)

#     #     for row in range(len(var_rows_dict[0])):
#     #         if not union_operators:
#     #             answer_arr.append(0) if 0 in exp_value_arr[row] else answer_arr.append(1)
#     #         else:
#     #             answer_arr.append(1) if 1 in exp_value_arr[row] else answer_arr.append(0)

#     #         var_rows_dict['answer'] = answer_arr
#     #     print(var_rows_dict)

#         var_rows = var_rows_dict.values()
#         calculations = pd.DataFrame(var_rows)
#         print(calculations.to_dict())
#         return calculations.to_dict()

# def get_variable_rows(operand_dict):
#         operands  = np.array(list(operand_dict.values()))
#         column_size = 2**operands.size
#         columns = np.zeros((operands.size, column_size))
        
#         indices = []
#         for i in range(operands.size):
#             alternations = 2**(i)
#             numbered_column = np.arange(0, column_size)
#             boolean_column = np.floor((numbered_column/alternations)%2)
#             columns[i] = boolean_column
#             indices.append(2*i)
    
#             row_arr = dict(zip(indices, np.flip(columns)))
#         return row_arr