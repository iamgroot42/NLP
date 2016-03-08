import facebook
import csv
import requests

ACCESS_TOKEN = "CAACEdEose0cBAMjmkaomn5FXRzTlWnVOHHQbPiFy33Lf11Po483AZAdEGSwDFVujhN0CY5mZCROJVEpOjTzeNs4KrU64l7nZCPsBQFaZAigApsLv7QmVDNhqx5DCyW8bLygecDD8jT5yax7AjZCZCQcciXTc2kZAt36ZChlwH35php032CIxnSblQ9ECYpsy7uv37iEiHKGBZAQZDZD"

graph = facebook.GraphAPI(ACCESS_TOKEN)


def get_all_posts(userID):
	node = userID + "/posts"
	allposts = []

	print userID + "/posts"

	data = graph.get_object(node)

	while True:
		try:
			for post in data['data']:
				try:
					allposts.append(post['message'])
				except:
					try:
						allposts.append(post['description'])
					except:
						continue
			data = requests.get(data['paging']['next']).json()
		except:
			break		

	allposts = [[post.encode("utf-8")] for post in allposts]

	with open('../Data/Raw/%s_posts.csv' % userID, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(allposts)
	

try:
	f = open("facebook_users","r")
	for handle in f:
		try:
			get_all_posts(handle.strip())
			print "Fetched posts for : ",handle
		except:
			print "Invalid user : ",handle
	f.close()
except:
	print "Username file not found"
