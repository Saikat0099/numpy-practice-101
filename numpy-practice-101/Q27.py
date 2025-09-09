#Create a 2D NumPy array and compute row-wise and column-wise sum.

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("2D Array:")
print(arr)

row_sum = np.sum(arr, axis=1)
print("\nRow-wise Sum:")
print(row_sum)

col_sum = np.sum(arr, axis=0)
print("\nColumn-wise Sum:")
print(col_sum)
