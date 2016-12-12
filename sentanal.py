import tweepy
from textblob import TextBlob 
import sys
import csv
import re

consumer_key = 'KLojskDD6g7bAqbq6H7U3xSFI'
consumer_secret = 'OhHYnffIezWxn9QCl5eLuOTdGNiFR8yLl3Q8wZSiBGuwkhCEHl'

access_token = '2536792886-RqEEyyxd9SajCUzw2VlKWQm4DeSJTRyD5wPzSqO'
access_token_secret = 'R6jkmz00V4eC286QR9cmZ0DWiX9TdoQukLbF4z3wtwHSo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

# for tweet in public_tweets:
# 	print(tweet.text)
# 	analysis = TextBlob(tweet.text)
# 	print(analysis.sentiment)
# 	print("\n")

def cleanTweet(tweet):

	tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
	return tweet


with open('sent.csv','w') as f:

	writer = csv.DictWriter(f,fieldnames=['Tweet','Sentiment'])

	writer.writeheader()

	for tweet in public_tweets:

		text = cleanTweet(tweet.text)
		analysis = TextBlob(text)
		polarity = analysis.sentiment.polarity

		if(polarity >= 0):
			sentiment = 'positive'
		else:
			sentiment = 'negative'

		writer.writerow({'Tweet':text, 'Sentiment':sentiment})

