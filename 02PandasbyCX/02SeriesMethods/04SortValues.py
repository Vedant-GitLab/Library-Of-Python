#iska use sbse jyada ya sbse kam data nikalne ke liye krte hai.
#ye example bhi thik hai pr hum runs wala example bhhi le skte hai
import pandas as pd
movies=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\bollywood_actors_movies.csv')
print(movies['Actor Name'].sort_values(ascending=False))
print(movies['Actor Name'].sort_values(ascending=False).head(1))
print(movies['Actor Name'].sort_values(ascending=False).head(1).values[0])