#Write a program to sort a NumPy array by row and column.

import numpy as np
arr = np.array([[12, 5, 7],
                [3, 8, 1],
                [6, 4, 9]])

print("Original Array:")
print(arr)

row_sorted = np.sort(arr, axis=1)
print("\nArray sorted by rows:")
print(row_sorted)

col_sorted = np.sort(arr, axis=0)
print("\nArray sorted by columns:")
print(col_sorted)
