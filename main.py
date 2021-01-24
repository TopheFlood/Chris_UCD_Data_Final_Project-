import pandas as pd

data= pd.read_csv("avacados_data.csv")
#First look at data
print(data.head())

# to see the largest average price it was 3.25
print(data["AveragePrice"].max())





