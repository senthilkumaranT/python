
import pandas as pd


data = pd.read_csv("/content/weather_data_nyc_centralpark_2016(1).csv")
data

data["maximum temperature"].max()

data["date"][data["average temperature"] > 55 ]

data["maximum temperature"].mean()


data.isnull().sum()


data.shape


data.columns

data.head()

data.tail()


data[2:5]