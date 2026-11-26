import pandas as pd
vk=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\vk.csv')

#Sum : Saare items ka sum kr dega
print(vk['Runs'].sum(), " --->  Total Runs")

#Product : Saare items ko multiply kr dega
print(vk['Runs'].product(), " --->  Total Runs")
