#https://www.kaggle.com/neuromusic/avocado-prices was the source of my data
import pandas as pd

data= pd.read_csv("avacados_data.csv")
#First look at data
#print(data.head())

#looked at the shape of the the data (18249,14)
#print(data.shape)

#Importing from Twitter
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