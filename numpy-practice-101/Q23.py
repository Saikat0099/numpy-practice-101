#Write a program to generate a matrix of size 6×6 with checkerboard pattern (0,1).

import numpy as np
checkerboard = np.zeros((6,6), dtype=int)

checkerboard[::2, 1::2] = 1  
checkerboard[1::2, ::2] = 1 

print("6x6 Checkerboard Pattern:")
print(checkerboard)
