import numpy as np
m=np.array([1,2,3,4,5])
n=np.array([3,4,5,6,7])
print(m,n)

#UNION 1D
Union = np.union1d(m,n) #common elements ko single time hi lega
print(Union, "-> is Union")

#Intersect 1D
Intersection = np.intersect1d(m,n) #jo dono me common hai wahi print hoga
print(Intersection, "-> is Intersection")

#Setdiff 1D
SetDifference = np.setdiff1d(m,n) #jo m hai pr n mein nhi 
print(SetDifference,"-> is SetDifference")
print(np.setdiff1d(n,m),"-> is SetDifference")

#Setxor 1D
Setxor = np.setxor1d(m,n) #common ko hatake baaki sbko rkhega
print(Setxor,"-> is Setxor")

#in1D : we use in1D as isin
In1D = np.isin(m,1) #ye dekhta hai ki given set operator mein hai ya nhi
print(In1D, "-> is In1D")
print(m[np.isin(m,1)], "-> is In1D")
print(np.isin(n,10), "-> is In1D")