# -*- coding: utf-8 -*-

import nltk
import pickle
import json

f = open('classifier_hin.pickle', 'rb')
classifier = pickle.load(f)
f.close()

f = open('word_features_hin.pickle', 'rb')
word_features = pickle.load(f)
f.close()

emoticons = {":)":"positive",":(":"negative",":|":"neutral",":*":"positive","<3":"positive",":-)":"positive",":'(":"negaitve","-_-":"neutral",":-(":"negative"}

def extract_features(document):
	global word_features
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features


def getSentiment( text):
	text = json.loads( json.dumps([text]))[0]
	dist = classifier.prob_classify(extract_features(text.split()))
	d = {"positive":0,"negative":0,"neutral":0}
	emoti_found = False
	for x in emoticons:
		if x in text:
			d[emoticons[x]] += 1
			emoti_found = True
	if emoti_found:
		if d["positive"] > d["negative"]:
			return "positive"
		elif d["positive"] < d["negative"]:
			return "negative"
	# print text
	# for label in dist.samples():
		# print label," ",str(dist.prob(label))
	return three_label(dist.prob("positive"),dist.prob("negative"))


def three_label(val1,val2):
	# print str(val1) + " and " + str(val2)
	if abs(val1-val2)<=0.08:
		return "neutral"
	elif val1>val2:
		return "positive"
	else:
		return "negative"


def getEntity(s):
	return getSentiment(s)

if __name__ == "__main__":
	print "Enter Input"
	while True:
		print getSentiment( raw_input()  ) 
