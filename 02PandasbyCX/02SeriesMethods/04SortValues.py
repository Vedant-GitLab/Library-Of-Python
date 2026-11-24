#iska use sbse jyada ya sbse kam data nikalne ke liye krte hai.
#ye example bhi thik hai pr hum runs wala example bhhi le skte hai
import pandas as pd
vk=pd.read_csv(r'C:\Users\tiwar\OneDrive\Desktop\Libraries\02PandasbyCX\02SeriesMethods\vk.csv')
# print(vk['Runs'].sort_values())
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(vk['Runs'].sort_values(ascending=False))
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(vk['Runs'].sort_values(ascending=False).head(1))
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(vk['Runs'].sort_values(ascending=False).head(1).values[0])
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(vk)

#sort Values sirf temporary changes krta hai orginal file me chnges nhi hote
#waise humko changes nhi krna chahiye pr kbhi kbhi krna pade toh hum inplace metrhod ka use krte hai qki pandas humko option deta hai isse hum original file me changekr skte hai

#Inplace 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(vk['Runs'].sort_values(inplace=True)) #inplace true krne se ye permanent operation ho jayega hamare original series me changes ho jayenge
      #ye error d erha hai 