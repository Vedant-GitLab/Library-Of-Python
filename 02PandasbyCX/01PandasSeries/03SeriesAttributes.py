import numpy as np
import pandas as pd
marks = {
    'maths':67,
    'english':45,
    'hindi':89,
    'science':67
    }

print(type(marks))

#convert dict into series qki attributes sirf series pr hi kaam krte hai
series = pd.Series(marks, name='vedant ke marks')
print(type(series))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#01 size : how many items or values are in series
print(series.size, " ---> SIZE")

#02 dtype : series ke andar ke items ka datype btata hai
print(series.dtype, " ---> DTYPE")

#03 Name : Series object ka ky naam hai 
print(series.name, "---> NAME")

#04 is_unique : series ke saare items unique hai ya nhi
print(series.is_unique, "---> IS_UNIQUE")  #qki math aur science ki values equal hai

a = pd.Series([1,2,3,4,5])
print(a.is_unique, "---> IS_UNIQUE")

#05 index : ek saath saath sare ke sare index provide kr dega
print(series.index, "---> INDEX")

runs = [13, 24, 123, 34, 443] #second example
runs_ser = pd.Series(runs)
print(runs_ser.index, "---> INDEX")

#06 values : ek saath saath sare ke sare values provide kr dega
print(series.values, "---> VALUES")
print(type(series.values))

runs = [13, 24, 123, 34, 443] #second example
runs_ser = pd.Series(runs)
print(runs_ser.values, "---> VALUES")
print(type(runs))