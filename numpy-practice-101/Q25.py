#Create a 1D array of 20 elements and reverse it without using Python slicing.

import numpy as np

arr = np.arange(1, 21)

print("Original Array:")
print(arr)

reversed_arr = np.flip(arr)

print("\nReversed Array:")
print(reversed_arr)
