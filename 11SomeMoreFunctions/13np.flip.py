#The numpy.flip() function reverses the order of array elements along the specified axis, preserving the shape of the array.

import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
print(np.flip(a))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
b = np.arange(24).reshape(6,4)
print(b)
print(np.flip(b))
print(np.flip(b, axis=0))
print(np.flip(b, axis=1))
