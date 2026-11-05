#The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis.
#syntax : numpy.delete(arr,obj,axis=none)
import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
print(np.delete(a,[1])) #delete the item at index 1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
b = np.arange(24).reshape(6,4)
print(b)
print(np.delete(b,[1],axis=1)) #delete the column of index 1
print(np.delete(b,[1],axis=0)) #delete the row of index 0