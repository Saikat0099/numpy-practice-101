#Write a NumPy program to check whether two arrays are equal element-wise.

import numpy as np

# Create two sample arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 0, 4])

print("Array 1:", arr1)
print("Array 2:", arr2)

equal_elements = np.equal(arr1, arr2)

print("\nElement-wise Equality:")
print(equal_elements)

all_equal = np.array_equal(arr1, arr2)
print("\nAre all elements equal?:", all_equal)
