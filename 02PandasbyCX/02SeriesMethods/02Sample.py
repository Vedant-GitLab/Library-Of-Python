#iska use series me se randomly koi ek ya usse jyada row ya data nikalne ke liye use hota hai
import pandas as pd
df=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\student.csv')
print(df)
print("*******************************************")
print(df.sample()) #randomly koi 1 dega
print("*******************************************")
print(df.sample(2)) #randomly koi 2 dega