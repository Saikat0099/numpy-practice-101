#Generate a random 3×3 matrix and find its determinant.

import numpy as np
matrix = np.random.randint(1, 10, (3, 3))  # values between 1 and 9
print("Random 3x3 Matrix:")
print(matrix)

det = np.linalg.det(matrix)
print("\nDeterminant of the matrix:", det)
