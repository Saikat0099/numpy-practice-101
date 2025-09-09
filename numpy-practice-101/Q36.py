#Create a 2D array and apply broadcasting to add a 1D array.

import numpy as np

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

arr1d = np.array([10, 20, 30])

print("Original 2D Array:")
print(arr2d)
print("\n1D Array to Add:")
print(arr1d)

result = arr2d + arr1d

print("\nResult after Broadcasting Addition:")
print(result)
