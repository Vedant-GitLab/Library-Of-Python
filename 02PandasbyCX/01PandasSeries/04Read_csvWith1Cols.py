#isme hum ye jante hai ki "series ko hum kaise bna skte hai using existing datasets"

#read_csv = iska kaam hota hai csv files jko read krna
#csv(comma seperated values) : basically excel jaisi files jaha pr saari values comma seperated hoti hai
import pandas as pd

df=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\01PandasSeries\students.csv') #this r is used for raw string because Python mein \U, \n, \t jaise characters special escape sequences hote hain. Tumhare path mein \Users hai, jahan \U ko Python Unicode escape samajh raha hai.
print(df)
print(type(df)) #data frame
#isko series me convert krne ke liye squeeze=True krna padega last me ' , ' lgakr