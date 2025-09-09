#Create a NumPy array with values from 0 to 20 and replace all even numbers with -1.


import numpy as np
arr = np.arange(21)

print("Original Array:")
print(arr)

arr[arr % 2 == 0] = -1

print("\nArray after replacing even numbers with -1:")
print(arr)
