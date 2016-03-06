import facebook
import csv

ACCESS_TOKEN = "CAACEdEose0cBAFfgprOpw3ZCGdMp75kNfpS0JDaJ5NPQIO3OlZBghoBZC75fcHZAYeG9DDAEohW0coxyAGwjQ4VkKyRQXWcZCZC6L8ZBINDj9DG0LOyXlCDnpL6kfr6VJM5LwLXpgZBoII6xkXrBZAKsBjGZBcZAHZCqtrC8KizUO3iBPqw0YZCbIw3c1kLeqUyCBTtAtXeaUcqYekgZDZD"

graph = facebook.GraphAPI(ACCESS_TOKEN)


def get_all_posts(userID):
	node = userID + "/posts"
	allposts = []

	while True:
		try:
			data = graph.get_object(node)
			for post in data['data']:
				try:
					allposts.append(post['message'])
				except:
					try:
						allposts.append(post['description'])
					except:
						continue
			node = data['paging']['next']	
		except:
			break		

	allposts = [[post] for post in allposts]

	with open('../Data/Raw/%s_posts.csv' % userID, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(allposts)
	

try:
	f = open("facebook_users","r")
	for handle in f:
		try:
			get_all_posts(handle)
			print "Fetched posts for : ",handle
		except:
			print "Invalid user : ",handle
	f.close()
except:
	print "Username file not found"
