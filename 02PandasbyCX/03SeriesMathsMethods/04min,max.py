import pandas as pd
vk=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\vk.csv')
movies=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\03SeriesMathsMethods\bollywood_actors_movies.csv')

print(vk['Runs'].max()) #maximum nikalta hai
print(vk['Runs'].min()) #minimum nikalta hai
print(movies['Actor Name'].max())
print(movies['Actor Name'].min())