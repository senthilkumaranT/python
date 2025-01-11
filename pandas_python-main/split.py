# find the maximum temperature in each of the cities

# find the average wind speed per city


import pandas as pd


data = pd.read_excel("/content/split.xlsx")
data

g=data.groupby("city")
g


for city ,city_df in g:
  print(city)
  print(city_df)
  
  
g.max()


g["windspeed"].mean()