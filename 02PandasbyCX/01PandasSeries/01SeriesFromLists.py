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

