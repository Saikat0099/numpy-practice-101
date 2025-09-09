#Create a 3×3 matrix and compute its inverse using NumPy.

import numpy as np
A = np.array([[4, 7, 2],
              [3, 5, 1],
              [2, 8, 9]])

print("Original Matrix (A):")
print(A)

A_inv = np.linalg.inv(A)
print("\nInverse of Matrix (A⁻¹):")
print(A_inv)

identity = np.dot(A, A_inv)
print("\nVerification (A × A⁻¹):")
print(identity)
