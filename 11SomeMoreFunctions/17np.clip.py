#numpy.clip() function is used to Clip (limit) the values in an array. (ye ek range me value ko rkhta hai)
import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
print(np.clip(a,a_min=25,a_max=75)) #puttng values in range of 25 to 75. means greater than 75 is equal to 75 and smaller than 25 is equal to 25