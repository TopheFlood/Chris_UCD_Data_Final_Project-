#https://www.kaggle.com/neuromusic/avocado-prices was the source of my data
import pandas as pd

data= pd.read_csv("avacados_data.csv")
#First look at data
print(data.head())

#looked at the shape of the the data (18249,14)
print(data.shape)

#Created a for loop
for lab, row in data.iterrows():
    print(str(lab) + ": " + str(row["region"]))

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
print(organic.shape)

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

print(data.sort_index())

#sorted data by region
data_sorted_region= (data.sort_index(level="region"))

#sliced using iloc to show the first 10 rows
print(data_sorted_region.iloc[0 : 10])

import numpy as np

#Used numpy for average price 1.405978409775878
np_average_price= np.array(data["AveragePrice"]).mean()

print(np_average_price)

#used numpy array to print if < 1.4 or not
cheap= np.array(data["AveragePrice"]< 1.4)

print(cheap)

#used sort index on year
date_ind = data.set_index("year").sort_index()

#used loc to print years between 2015 and 2016
print(date_ind.loc["2015":"2016"])

West = data[(data["region"]== "West")]

print(West.head())
print(West.shape)

#Found total volume of West 1086779155.75
total_west_volume= West["Total Volume"].sum()
print(total_west_volume)

Total_US = data[(data["region"]== "TotalUS")]
print(Total_US.head())
print(Total_US.shape)

#Found total volume un US 5864740181.799999
total_us_volume= Total_US["Total Volume"].sum()
print(total_us_volume)

#west_us_total_merge = total_us_volume.merge(total_west_volume, on= ["Date", "region"])

print(west_us_total_merge.head())

new_data = data[["AveragePrice","Total Volume","Total Bags","Small Bags","Large Bags","XLarge Bags","type","year","region"]]

print(new_data.head())

volume_grater_than_100000 = new_data[new_data["Total Volume"] > 100000]

#printed the data
print(volume_grater_than_100000.head())
#(9301, 9)
print(volume_grater_than_100000.shape)
import seaborn as sns

sns.set_style("whitegrid")

g= sns.relplot(x= "year",
            y= "AveragePrice",
            data= new_data,
            kind= "line",
            hue= "type",
            size= "type",
            ci= None)

g.fig.suptitle("Avacados by type and average cost")
g.set(xlabel="Year",
       ylabel="Average price")

plt.show()
sns.set_style("whitegrid")

g= sns.relplot(x= "year",
            y= "Total Volume",
            data= new_data,
            kind= "line",
            hue= "type",
            size= "type",
            ci= None)

g.fig.suptitle("Avacados by type and total volume")
g.set(xlabel="Year",
       ylabel="Total volume")

plt.show()

import tweepy, json

access_token = "47938335-81XwL5Sx0SgTI5Z4luyMj5Ze8ASCQDB5I3EjeRsL5"
access_token_secret = "tDgPRvsBcT8OUQ2eqN478mxbaMzDayh29hUQzjfSStQ5D"
API_key = "pGy2gOdu42r4nNmHW11Nj1yYP"
API_secret = "Q5dJvRGC29V4qc0I8AC9oZWQpllAjTFvK9swQpLKTL3mStfSWf"


auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

l = MyStreamListener()

stream = tweepy.Stream(auth, l)

stream.filter(track=['gamestop'])

tweets_data_path = 'tweets.txt'

tweets_data = []

tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

tweets_file.close()

print(tweets_data[0].keys())

df = pd.DataFrame(tweets_data, columns=['text','lang'])

print(df.head())