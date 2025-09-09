#Write a NumPy program to compute numerical gradient of a 1D array.

import numpy as np

arr = np.array([0, 1, 4, 9, 16, 25])

print("Original Array:")
print(arr)

grad = np.gradient(arr)

print("\nNumerical Gradient of the Array:")
print(grad)
