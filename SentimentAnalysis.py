import tweepy
from textblob import TextBlob

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'

access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('thoothukudi')

storage_dir = "repo.csv"
csv = open(storage_dir,"w")
columnTitle = "Tweet, Positivity\n"
csv.write(columnTitle)

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment.polarity)
	if analysis.sentiment.polarity > 0 :
		verdict = "positive"
	else :
		verdict = "negative"
	to_write = tweet.text+", "+ verdict + "\n"
	csv.write(to_write.encode('utf-8'))


