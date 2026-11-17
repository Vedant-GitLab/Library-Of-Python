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

#size : how many items or values are in series
print(series.size, " ---> SIZE")

#dtype : series ke andar ke items ka datype btata hai
print(series.dtype, " ---> DTYPE")

# Name : Series object ka ky naam hai 
print(series.name, "---> NAME")

#is_unique : series ke saare items unique hai ya nhi
print(series.is_unique, "---> IS_UNIQUE")  #qki math aur science ki values equal hai
