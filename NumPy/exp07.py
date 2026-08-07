import numpy as np

x = np.array([[1,0],[0,1]])
print("Array", x)
print("\nsum of all elements: ", np.sum(x))
print("\nsum of each columns: ", np.sum(x, axis = 0))
print("\nsum of each rows: ", np.sum(x, axis = 1))