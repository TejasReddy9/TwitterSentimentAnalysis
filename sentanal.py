import tweepy
from textblob import TextBlob 
import sys
import csv
import re

if len(sys.argv) >= 2:
	topic = sys.argv[1]
else:
	print('I\'ve assumed topic as Trump')
	topic = 'Trump'

consumer_key = open('consumer_key.txt','r').read()
consumer_secret = open('consumer_secret.txt','r').read()

access_token = open('access_token.txt','r').read()
access_token_secret = open('access_token_secret.txt','r').read()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(topic)

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

