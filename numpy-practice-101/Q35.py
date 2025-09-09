#Generate a random dataset of 1000 numbers and compute histogram using NumPy.

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)  # mean=0, std=1

hist, bin_edges = np.histogram(data, bins=10)  # 10 bins

print("Histogram Counts:", hist)
print("Bin Edges:", bin_edges)

plt.hist(data, bins=10, edgecolor='black')
plt.title("Histogram of 1000 Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
