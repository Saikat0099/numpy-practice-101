#Create a 2D array and flatten it using ravel() and flatten().

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original 2D Array:")
print(arr)

ravel_arr = arr.ravel()
print("\nFlattened Array using ravel():")
print(ravel_arr)

flatten_arr = arr.flatten()
print("\nFlattened Array using flatten():")
print(flatten_arr)

ravel_arr[0] = 100
print("\nModified ravel array:")
print(ravel_arr)

print("\nOriginal Array after modifying ravel result (changes reflect):")
print(arr)

print("\nOriginal Array after modifying flatten result (no change):")
flatten_arr[0] = 200
print(flatten_arr)
print(arr)
