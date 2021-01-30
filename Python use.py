import numpy as np

#Used numpy for average price 1.405978409775878
np_average_price= np.array(data["AveragePrice"]).mean()

#print(np_average_price)

#used numpy array to print if < 1.4 or not
cheap= np.array(data["AveragePrice"]< 1.4)

#print(cheap)