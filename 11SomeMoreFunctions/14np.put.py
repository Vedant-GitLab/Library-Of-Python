#The numpy.put() function replaces specific elements of an array with given values of p_array. Array indexed works on flattened array.
#basically yeh editting krta hai array mein changes krta hai

import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a, "-----> Before")

np.put(a,[0,1],[110,345])
print(a, "-----> After")
