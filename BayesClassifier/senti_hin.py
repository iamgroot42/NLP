# -*- coding: utf-8 -*-


import nltk
from random import shuffle

pos_tweets = []
neg_tweets = []
f = open("train_hin.txt")
for k in f.readlines():

	if " # @ # " in k:

		l = k.strip('.\n').split(' # @ # ')
		if k[0] == '1':
			pos_tweets.append((l[1],'positive'))
		else:
			neg_tweets.append((l[1],'negative'))
f.close()
pos_tweets = list(set(pos_tweets))
neg_tweets = list(set(neg_tweets))
print pos_tweets
shuffle(pos_tweets)
shuffle(neg_tweets)
pos_test = pos_tweets[int(len(pos_tweets)*0.8):]
neg_test = neg_tweets[int(len(neg_tweets)*0.8):]
pos_tweets = pos_tweets[:int(len(pos_tweets)*0.8)]
neg_tweets = neg_tweets[:int(len(neg_tweets)*0.8)]

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
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)


total = len(pos_test) + len(neg_test) 
hits = total

for (tweet,sentiment) in pos_test+neg_test:
	if classifier.classify(extract_features(tweet.split())) != sentiment:
		hits-=1

print "Accuracy: ",hits*100.0/total,"%"