#Generate a 1D array and normalize it (scale values between 0 and 1).

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:")
print(arr)

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("\nNormalized Array (values between 0 and 1):")
print(normalized)
