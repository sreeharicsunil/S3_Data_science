import numpy as np

x = np.arange(16).reshape((4,4))
print("Array", x)
header = 'C1 C2 C3 C4'
np.savetxt('array.txt', x, fmt = "%d", header=header)
print("\nAfter loading, content of the text file: ", np.loadtxt('array.txt'))