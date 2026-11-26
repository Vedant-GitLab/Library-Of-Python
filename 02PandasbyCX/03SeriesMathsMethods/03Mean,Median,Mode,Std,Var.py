import pandas as pd
vk=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\vk.csv')
movies=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\03SeriesMathsMethods\bollywood_actors_movies.csv')

print(vk["Runs"].mean()) #Average, means approx runs per match 
print(vk["Match_No"].median())
print(movies['Actor Name'].mode()) #highest frequent item (Sbse jyada movie kis actor ki hai)
print(vk['Runs'].std())
print(vk['Runs'].var())