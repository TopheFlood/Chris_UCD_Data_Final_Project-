import numpy as np

#Used numpy for average price 1.405978409775878
np_average_price= np.array(data["AveragePrice"]).mean()

print(np_average_price)

#used numpy array to print if < 1.4 or not
cheap= np.array(data["AveragePrice"]< 1.4)

#print(cheap)

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

new_data = data[["AveragePrice","Total Volume","Total Bags","Small Bags","Large Bags","XLarge Bags","type","year","region"]]

print(new_data.head())

volume_grater_than_100000 = new_data[new_data["Total Volume"] > 100000]

#printed the data
print(volume_grater_than_100000.head())

#(9301, 9)
print(volume_grater_than_100000.shape)