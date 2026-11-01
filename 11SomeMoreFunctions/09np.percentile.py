#numpy.percentile()function used to compute the nth percentile of the given data (array elements) along the specified axis.

import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
print(np.percentile(a,100)) #means 100% sbse highest number jisse koi bda na ho
print(np.percentile(a,0)) #sbse minimum jisse chota koi na ho
print(np.percentile(a,50)) #iska mtlb 50% data peeche aur 50% hi data aage hoga
print(np.median(a),"median bhi a hi hai iska mtlb yahi beech ka no. hai")
print(np.percentile(a,75)) #means 75% data peeche hoga