#Create a 4×4 matrix with random integers and extract its upper triangular matrix.

import numpy as np
matrix = np.random.randint(1, 10, size=(4, 4))

print("Original 4x4 Matrix:")
print(matrix)

upper_tri = np.triu(matrix)

print("\nUpper Triangular Matrix:")
print(upper_tri)
