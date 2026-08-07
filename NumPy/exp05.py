import numpy as np

x = np.arange(21)
print("vectors")
print(x)
print("\nAfter changing the sign of the numbers in the range from a to b")
x[(x>=9) & (x<=15)] *= -1
print(x)