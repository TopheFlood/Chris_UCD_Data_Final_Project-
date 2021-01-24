#https://www.kaggle.com/neuromusic/avocado-prices was the source of my data
import pandas as pd

data= pd.read_csv("avacados_data.csv")
#First look at data
print(data.head())

# to see the largest average price it was 3.25
print(data["AveragePrice"].max())

#checked for missing values
print(data.isna())

#checked by column
print(data.isna().any())

#imported matplotlib
import matplotlib.pyplot as plt

#Made barchart to confirm no missing data
data.isna().sum().plot(kind="bar")

#To show graph
plt.show()
#To save the graph
plt.savefig()

#created new dataframe by organic
organic= data[(data["type"]== "organic")]

#printed the new dataframe
print(organic.head())

#created new dataframe by conventional
conventional= data[(data["type"]== "conventional")]

#printed the new data frame
print(conventional.head())

#Found mean of average price 1.405978409775878
print(data["AveragePrice"].mean())

#found median of average price 1.37
print(data["AveragePrice"].median())

#found mean of conventional average price 1.1580396668858208
print(conventional["AveragePrice"].mean())

#found mean of organic average price 1.6539986846432095
print(organic["AveragePrice"].mean())

#found median of conventional average price 1.13
print(conventional["AveragePrice"].median())

#found median of organic average price 1.63
print(organic["AveragePrice"].median())