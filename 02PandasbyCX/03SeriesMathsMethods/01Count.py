#count : Total number of items count krke deta hai series ke andr. Size bhi same kaam krta hai but count missing values ko count nhi krta pr size krta hai.
import pandas as pd
vk=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\vk.csv')
print(vk.count())