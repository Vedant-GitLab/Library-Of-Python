#Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.

import numpy as np
a = np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(a)
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100])) #iska mtlb 0 se 10 ke beech kitne item hai, fir 10 se 20 ke beech, fir 20 se 30 ke beech, fir 30 se 40 ke beech aise hi krte krte 90 se 100 ke beech, aur yaha bins ka mtlb kitne numbers hai us range me.
print(np.histogram(a,bins=[0,50,100])) #means 0 se 50 aur 50 se 100 ke beech kitne items hai.