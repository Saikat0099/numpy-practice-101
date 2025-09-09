#Find the indices of maximum and minimum values in a NumPy array.

import numpy as np
arr = np.array([10, 25, 7, 30, 15, 5, 40])

print("Array:", arr)

max_index = np.argmax(arr)
print("Index of Maximum Value:", max_index)
print("Maximum Value:", arr[max_index])

min_index = np.argmin(arr)
print("Index of Minimum Value:", min_index)
print("Minimum Value:", arr[min_index])
