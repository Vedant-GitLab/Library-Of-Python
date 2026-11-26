import pandas as pd
vk=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\vk.csv')
print(vk['Runs'].max())
print(vk['Runs'].min())