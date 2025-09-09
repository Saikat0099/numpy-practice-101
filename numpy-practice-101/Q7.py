#Create two 3×3 matrices and perform matrix multiplication.

import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

result = np.dot(A, B)
print("\nMatrix Multiplication (A x B):")
print(result)
