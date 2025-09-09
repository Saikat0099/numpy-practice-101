#Write a NumPy program to generate a random permutation of numbers 1 to 10.

import numpy as np
arr = np.arange(1, 11)

perm = np.random.permutation(arr)

print("Original Array (1 to 10):")
print(arr)

print("\nRandom Permutation:")
print(perm)
