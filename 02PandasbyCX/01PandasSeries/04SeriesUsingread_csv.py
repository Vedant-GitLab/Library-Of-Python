#isme hum ye jante hai ki "series ko hum kaise bna skte hai using existing datasets"

#read_csv = iska kaam hota hai csv files jko read krna
#csv(comma seperated values) : basically excel jaisi files jaha pr saari values comma seperated hoti hai
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
#ye error dega