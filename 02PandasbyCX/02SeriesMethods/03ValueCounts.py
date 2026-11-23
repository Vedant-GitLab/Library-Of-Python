#iska use hum values ke count ke liye krte jb humko check krna hota hai ki konsi value data mein kitni baar aayi hai. It araanges data ascending order conclusionally hum frequency count nikalte hai data ka
import pandas as pd
movies=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\bollywood_actors_movies.csv')
print(movies['Actor Name'].value_counts())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(movies)