#Generate two 1D arrays and compute cosine similarity using NumPy.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("\nCosine Similarity between a and b:", cos_sim)

