#Create a 4×4 array and rotate it by 90 degrees using NumPy.

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Original 4x4 Array:")
print(arr)

rotated_arr = np.rot90(arr)

print("\nArray after 90-degree rotation:")
print(rotated_arr)
