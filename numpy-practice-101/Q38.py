#Create two arrays and find Pearson correlation coefficient using NumPy.

import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

print("Array x:", x)
print("Array y:", y)

corr_matrix = np.corrcoef(x, y)
pearson_corr = corr_matrix[0, 1]

print("\nPearson Correlation Coefficient between x and y:", pearson_corr)
