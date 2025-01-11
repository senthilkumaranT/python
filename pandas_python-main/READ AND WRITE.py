import pandas as pd

data = pd.read_csv("/content/weather_data_nyc_centralpark_2016(1).csv" ,header=None , names = ["date", "maximum temperature", "minimum temperature", "average temperature", "precipitation", "snow fall", "snow depth"],nrows=10
)
data