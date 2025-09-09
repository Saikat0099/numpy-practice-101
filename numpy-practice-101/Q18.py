#Generate a 5×5 random matrix and compute its trace.

import numpy as np
matrix = np.random.rand(5, 5)

print("5x5 Random Matrix:")
print(matrix)

trace_val = np.trace(matrix)

print("\nTrace of the Matrix:", trace_val)
