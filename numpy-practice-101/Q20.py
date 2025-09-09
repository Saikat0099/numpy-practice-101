#Create a 3D array of shape (3,3,3) and find its mean across axis=0.


import numpy as np
arr = np.random.randint(1, 10, size=(3, 3, 3))

print("3D Array (3x3x3):")
print(arr)

mean_axis0 = np.mean(arr, axis=0)

print("\nMean across axis=0:")
print(mean_axis0)
