#Head Aur Tail Ka Use Upar Ya Neeche Se Selected Rows Ko Print Krane Ke Liye Use Hota Hai
import pandas as pd
df=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\student.csv')
print(df)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(df.head) #upar ki rows print krga
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(df.head(2)) #upar se 2 row print krega
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(df.tail(2)) #neeche se 2 row print krega
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(df.tail(4)) #neeche se 4 row print krega