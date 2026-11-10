#With the help of numpy.isin() method, we can see that one array having values are checked in a different numpy array having different elements with different sizes.

import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
item = 10,20,30,40,50,60,70 #this function is used to search the given items in given array, here we have 10,20,30,40,50,60,70 so in these items which are in "a" gives true otherwise false
print(np.isin(a,item)) #it gives answer in true or false
print(a[np.isin(a,item)]) #it gives the items which are in "a"