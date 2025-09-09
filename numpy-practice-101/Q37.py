#Write a program to find unique values and their counts in a NumPy array.

import numpy as np
arr = np.array([1, 2, 2, 3, 4, 4, 4, 5, 1, 2])

print("Original Array:")
print(arr)

unique_values, counts = np.unique(arr, return_counts=True)

print("\nUnique Values:", unique_values)
print("Counts:", counts)
