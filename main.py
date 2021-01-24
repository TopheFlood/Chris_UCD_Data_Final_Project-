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

#used drop duplicates to see the individual if every region had both types type
regions = data.drop_duplicates(subset = ["region" ,"type"])

print(regions.head())

#counted the number of regions that had each type
region_counts = regions["region"].value_counts()

#prnted the count for regions and type
print(region_counts)

#found the amount in each type conventional 9126 organic 9123
type_counts = data["type"].value_counts()

#printed the type count
print(type_counts)

#found the total volume for conventional 15087220911.31
conventional_volume= conventional["Total Volume"].sum()

#printed conventional value
print(conventional_volume)

#found the total volume of organic 436181682.0899999
organic_volume= organic["Total Volume"].sum()

print(organic_volume)

#found total volume
total_volume= data["Total Volume"].sum()

print(total_volume)

#found total volume by type
volume_by_type = data.groupby("type")["Total Volume"].sum()

#printed data
print(volume_by_type)

#found proportion of sales by type conventional 0.971902 organic 0.028098
proportion_of_vol_by_type= volume_by_type/total_volume

#printed data
print(proportion_of_vol_by_type)