#Write a NumPy program to split a 1D array into 3 equal parts.

import numpy as np
arr = np.arange(1, 13)

print("Original Array:")
print(arr)

parts = np.split(arr, 3)

print("\nArray split into 3 equal parts:")
for i, part in enumerate(parts, start=1):
    print(f"Part {i}:", part)
