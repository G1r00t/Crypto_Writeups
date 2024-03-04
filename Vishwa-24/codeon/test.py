import numpy as np

import numpy as np
# Matrix A
matrix_a = np.array([
    [45, 35, 93, 95, 24, 65],
    [25, 15, 55, 64, 36, 45],
    [15, 65, 62, 16, 65, 38],
    [19, 64, 35, 69, 65, 63],
    [47, 67, 48, 60, 39, 27],
    [66, 48, 77, 22, 10, 69]
])
# Matrix B
matrix_b = np.array([
    [33, 25, 30, 11, 68, 65],
    [83, 36, 19, 33, 55, 51],
    [20, 16, 48, 63, 41, 71],
    [30, 42, 12, 25, 31, 37],
    [51, 3, 44, 23, 43, 85],  # Corrected typo in the provided matrix
    [20, 39, 28, 41, 1, 70]    # Corrected typo in the provided matrix
])


# Multiplication (Element-wise)
matrix_elementwise_product = matrix_a * matrix_b
print("\nMatrix Element-wise Multiplication:\n", matrix_elementwise_product)
import numpy as np
# Given matrix element-wise multiplication
matrix_result = np.array([
    [1485, 875, 2790, 1045, 1632, 4225],
    [2075, 540, 1045, 2112, 1980, 2295],
    [300, 1040, 2976, 1008, 2665, 2698],
    [570, 2688, 420, 1725, 2015, 2331],
    [2397, 201, 2112, 1380, 1677, 2295],
    [1320, 1872, 2156, 902, 10, 4830]
])
# [69,49,76,101,98,95]
# [69,68,101,106,92,53]
# [64,96,26,64,69.102]
# [98,92,66,73,9,89]
# [37,83,106,82,25,53]
# [22,102,32,76,10,110]
import numpy as np
# Given matrix element-wise multiplication
matrix_result = np.array([
    [1485, 875, 2790, 1045, 1632, 4225],
    [2075, 540, 1045, 2112, 1980, 2295],
    [300, 1040, 2976, 1008, 2665, 2698],
    [570, 2688, 420, 1725, 2015, 2331],
    [2397, 201, 2112, 1380, 1677, 2295],
    [1320, 1872, 2156, 902, 10, 4830]
])
# Take the modulus of each element with 118
matrix_result_mod = np.mod(matrix_result, 118)
print(matrix_result_mod)