import pandas as pd
movies=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\bollywood_actors_movies.csv')
print(movies)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(movies.sort_index()) #isme error aa rha hai
print(movies.sort_values(by='Actor Name'))
