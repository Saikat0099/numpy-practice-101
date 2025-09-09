#Write a program to find the cumulative sum of a NumPy array.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])

print("Original Array:")
print(arr)

cumsum_arr = np.cumsum(arr)

print("\nCumulative Sum of the Array:")
print(cumsum_arr)
