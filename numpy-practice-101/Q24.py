#Generate a 3×3 random matrix and apply element-wise square root.

import numpy as np
matrix = np.random.randint(1, 10, size=(3, 3))

print("Original 3x3 Matrix:")
print(matrix)

sqrt_matrix = np.sqrt(matrix)

print("\nElement-wise Square Root of the Matrix:")
print(sqrt_matrix)
