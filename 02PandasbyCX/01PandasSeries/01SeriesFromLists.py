import numpy as np
import pandas as pd
#hum hamesha numpy aur pandas ko saath me hi import krenge qki jyadatar dono ka use padta hai. Hum sirf pandas ka bhi use kr skte hai


#string
country = ['India', 'USA', 'Pakistan', 'Sri Lanka', 'Nepal ']
print(pd.Series(country)) #pd.series ki help se hum lists ko series me convert krte hai
#har item ke aage ek number hoga jise hum index of the item kahenge
#dtype: object means iska datatype object hai means string hai. 99% of the cases me hum string ko object kehte hai

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#integers
runs = [13, 24, 123, 34, 443]
print(pd.Series(runs))
#iska dtype: int64 means iska datatype integer hai 64 bits ka

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Custom Index
marks = [23, 45, 67, 78, 88]
subjects = ['maths', 'english', 'science', 'hindi', 'bio']
print(pd.Series(marks, index=subjects))
#agar humko kisi data ko index ki tarah use krna hoga to hum index=  ka use krenge

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Setting a name
marks = [23, 45, 67, 78, 88]
subjects = ['maths', 'english', 'science', 'hindi', 'bio']
print(pd.Series(marks, index=subjects, name='Vedant Ke marks')) # ye 'name' function koi additional data add krne ke liye use hota hai
marks2 = pd.Series(marks, index=subjects, name='Vedant Ke marks')
print(marks2)