#Generate a random 3×3 matrix and perform Singular Value Decomposition (SVD).

import numpy as np

A = np.random.rand(3, 3)

print("Original Matrix (A):")
print(A)

U, S, Vt = np.linalg.svd(A)

print("\nU Matrix:")
print(U)
print("\nSingular Values (S):")
print(S)
print("\nV^T Matrix:")
print(Vt)

S_matrix = np.zeros_like(A, dtype=float)
np.fill_diagonal(S_matrix, S)
A_reconstructed = U @ S_matrix @ Vt
print("\nReconstructed Matrix (U*S*V^T):")
print(A_reconstructed)
