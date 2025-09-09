#Generate a random 3×3 matrix and compute its rank.

import numpy as np

matrix = np.random.randint(1, 10, size=(3, 3))

print("3x3 Random Matrix:")
print(matrix)

rank = np.linalg.matrix_rank(matrix)

print("\nRank of the Matrix:", rank)
