import pandas as pd
movies=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\bollywood_actors_movies.csv')
print(movies)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(movies.sort_index(inplace=True))