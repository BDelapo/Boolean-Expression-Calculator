
# import numpy as np
# import pandas as pd
# import math





# ## Class that calculates the truth values of the terms. Accepts POST requests containing Term in json form and accepts GET requests
# ## for the resulting calculations


# def calculate(self, terms):
        
#         arr_term = np.array(list(terms.values()))
#         operators = np.in1d(arr_term, ['+', '-', '*', '/'])
#         operands = (operators == False)
#         operand_count = np.count_nonzero(operands == True)
        
#         column_size = 2**operand_count
#         columns = np.zeros((operand_count, column_size))
        
#         for i in range(operand_count):
#             alternations = 2**(i)
#             numbered_column = np.arange(0, column_size)
#             boolean_column = np.floor((numbered_column/alternations)%2)
#             columns[i] = boolean_column

#         row_arr = np.flip(columns)
#         print(row_arr.shape)

#         return pd.DataFrame(row_arr).to_dict()


print(1)

