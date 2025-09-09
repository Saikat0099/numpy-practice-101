#Write a program to reshape a 1D array of size 12 into a 3×4 matrix.

import numpy as np
arr = np.arange(1, 13) 
print("Original 1D Array:")
print(arr)

matrix = arr.reshape(3, 4)
print("\nReshaped 3x4 Matrix:")
print(matrix)
