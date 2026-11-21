import pandas as pd

df = pd.read_csv(
    r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\01PandasSeries\students.csv',
    index_col='City' #jis column ko aage rkhna hai usko likhenge ya fir 0 1 2 3 index de denge 
)

print(df)