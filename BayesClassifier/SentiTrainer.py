import nltk
from random import shuffle
import json
import pickle

pos_tweets = []
neg_tweets = []


# 'hindi_mov_reviews'  ,'tweet_neg_hin' , 'tweet_pos_hin' 
for x in [ 'tweet_from_emojis' ]:

	with open("../Data/formatted_groundtruth/"+x+".json") as data_file:    
		data = json.load(data_file)
		for l in data:
			if l['val'] == 'positive':
				pos_tweets.append((l['text'],'positive'))
			elif  l['val'] == 'negative':
				pos_tweets.append((l['text'],'negative'))
			print l['text'] + " =+> " + l['val']



print "Starting to train"

pos_tweets = list(set(pos_tweets))
neg_tweets = list(set(neg_tweets))
# print pos_tweets
shuffle(pos_tweets)
shuffle(neg_tweets)
pos_test = pos_tweets[int(len(pos_tweets)*0.7):]
neg_test = neg_tweets[int(len(neg_tweets)*0.7):]
pos_tweets = pos_tweets[:int(len(pos_tweets)*0.7)]
neg_tweets = neg_tweets[:int(len(neg_tweets)*0.7)]

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	tweets.append((words_filtered, sentiment))

def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

word_features = get_word_features(get_words_in_tweets(tweets))
def extract_features(document):
	# global word_features
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features


training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

f = open('classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()

f = open('word_features.pickle', 'wb')
pickle.dump(word_features, f)
f.close()



total = len(pos_test) + len(neg_test) 
hits = total
falsePos = 0
flaseNegs = 0
for (tweet,sentiment) in pos_test+neg_test:
	actual = classifier.classify(extract_features(tweet.split()))
	expected = sentiment
	if  actual != expected:
		hits-=1

	if actual == 'positive' and expected == 'negative':
		flaseNegs += 1
	if actual == 'negative' and expected == 'positive':
		falsePos += 1

	# if actual == 'negative' and expected == 'negative':
	# 	print tweet

print "Accuracy: ",hits*100.0/total,"%"
print "false negatives " + str(flaseNegs)
print "false positives " + str(falsePos)
print "total " + str(total)
print "Hits " + str(hits)


