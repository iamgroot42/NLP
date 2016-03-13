import sys
import tweepy
import csv
import json

from tweepy import OAuthHandler

consumer_key = 'VBju2cHaiEoRaeUNLtCv1BUTc'
consumer_secret = 'ucCQDSZ3HhVQRgIrBjBuNAOM230ezK4zdwCDEQnNt4Q1HiTR3G'
access_token = '364720387-JRbwpmThBqqeKJg0815aLIfuHO7Q9GK8QKEEHC0k'
access_secret = 'qWCQCWakD1gHHeFkGAkY0JN3Wvmu6geftR2GMo1oXFCq7'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# Source : https://gist.github.com/yanofsky/5436496
def save_all_tweets(screen_name):
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



def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	alltweets = []	
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1

	i = 0
	while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
		print "fetching ... " + str(i)
		i += 1

	outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]	
	return outtweets


def search_tweets( q):
	alltweets = []	
	new_tweets = api.search(q=q ,count=200 , result_type="recent" )
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1

	i = 0
	while len(new_tweets) > 0:
		new_tweets = api.search(q=q ,count=200 ,max_id=oldest , result_type="recent" )
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
		print "fetching ... " + str(i)
		i += 1

	jsonT = [ t.text for t in alltweets ]

	with open("../Data/emoji_tweets/tweet_"+q +".json"  , 'w') as outfile:
		json.dump(jsonT, outfile)



# search_tweets('mein :)')
# search_tweets('bacha :)')
# search_tweets('bacha :(')
# search_tweets('hamara :)')
# search_tweets('hamara :(')
# search_tweets('mera :)')
# search_tweets('mera :(')

# search_tweets('tha :)')
# search_tweets('tha :(')
# search_tweets('tha <3')
search_tweets('kharab :(')
search_tweets('udas :(')
# search_tweets('hai :)')
search_tweets('hai :(')
# search_tweets('film :)')
# search_tweets('pyar :)')
search_tweets('pyar :(')

# if __name__ == "__main__":

# 	try:
# 		f = open("twitter_users","r")
# 		for handle in f:
# 			try:
# 				save_all_tweets(handle)
# 				print "Fetched tweets for : ",handle
# 			except:
# 				print "Invalid handle : ",handle
# 	except:
# 		print "Username file not found"