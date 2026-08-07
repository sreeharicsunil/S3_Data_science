import numpy as np

x = np.array([3,5,1,2,3])
y = np.array([2,5,3,2,1])

print("Array A\n", x)
print("Array b\n", y)
print("\nA>B\n", np.greater(x,y))
print("\nA>=B\n", np.greater(x,y))
print("\nA<B\n", np.less(x,y))
print("\nA<=B\n", np.less_equal(x,y))