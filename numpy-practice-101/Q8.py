#Find eigenvalues and eigenvectors of a given 2×2 matrix using NumPy.

import numpy as np
A = np.array([[4, 2],
              [1, 3]])

print("Matrix A:")
print(A)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
