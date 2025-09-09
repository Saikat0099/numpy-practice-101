#Write a program to merge two NumPy arrays vertically and horizontally.

import numpy as np
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])

print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)

vertical_merge = np.vstack((arr1, arr2))
print("\nVertical Merge (vstack):")
print(vertical_merge)

horizontal_merge = np.hstack((arr1, arr2))
print("\nHorizontal Merge (hstack):")
print(horizontal_merge)
