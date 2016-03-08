import sys
import tweepy
import csv

from tweepy import OAuthHandler

consumer_key = 'zC0YU5Hgu4JKGYEMzEuVPmEjQ'
consumer_secret = 'KmTvJfjvkSXbhNIwRGkKokLxImfjyfozC9spDyiKheb7YEwtj8'
access_token = '4891935914-i6SmnOVQrOglkrh5eBfA79KqbGKaVezXd3D7kVV'
access_secret = 'Tk3VLo6vD3TbSYjSyXeWlwdfkZmGZqI0waTYgnkeMgaOL'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# Source : https://gist.github.com/yanofsky/5436496
def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	alltweets = []	
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1

	while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1

	outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]	
	with open('../Data/Raw/%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(outtweets)


try:
	f = open("twitter_users","r")
	for handle in f:
		try:
			get_all_tweets(handle)
			print "Fetched tweets for : ",handle
		except:
			print "Invalid handle : ",handle
except:
	print "Username file not found"