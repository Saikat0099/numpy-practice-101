#Write a NumPy program to create a 5×5 matrix with values 1,2,3,…,25.

import numpy as np
matrix = np.arange(1, 26).reshape(5, 5)

print("5x5 Matrix with values 1 to 25:")
print(matrix)
