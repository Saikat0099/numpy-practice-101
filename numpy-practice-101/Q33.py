#Create a 5×5 random matrix and normalize each row to have unit length.

import numpy as np
matrix = np.random.randint(1, 10, size=(5, 5))

print("Original 5x5 Matrix:")
print(matrix)

row_norms = np.linalg.norm(matrix, axis=1, keepdims=True)

normalized_matrix = matrix / row_norms

print("\nRow-normalized Matrix (unit length):")
print(normalized_matrix)

