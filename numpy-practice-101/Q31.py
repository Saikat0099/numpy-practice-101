#Write a program to create a structured NumPy array with fields (name, age, marks).

import numpy as np

# Define the data type for the structured array
dtype = [('name', 'U10'), ('age', 'i4'), ('marks', 'f4')]

# Create a structured array
students = np.array([('Saikat', 21, 85.5),
                     ('Taniya', 20, 90.0),
                     ('Anu', 20, 78.0)], dtype=dtype)

print("Structured Array:")
print(students)

print("\nNames:", students['name'])
print("Ages:", students['age'])
print("Marks:", students['marks'])
