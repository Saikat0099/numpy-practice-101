#Create a 5×5 matrix with random values and extract its diagonal elements.

import numpy as np
matrix = np.random.randint(1, 100, (5, 5))
print("Random 5x5 Matrix:")
print(matrix)

diagonal = np.diag(matrix)
print("\nDiagonal Elements:")
print(diagonal)
