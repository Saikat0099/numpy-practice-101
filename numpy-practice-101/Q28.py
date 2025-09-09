#Write a NumPy program to replace NaN values in an array with the mean of that column.

import numpy as np
arr = np.array([[1, 2, np.nan],
                [4, np.nan, 6],
                [7, 8, 9]], dtype=float)

print("Original Array:")
print(arr)

col_mean = np.nanmean(arr, axis=0)


inds = np.where(np.isnan(arr))

arr[inds] = np.take(col_mean, inds[1])

print("\nArray after replacing NaN with column mean:")
print(arr)
