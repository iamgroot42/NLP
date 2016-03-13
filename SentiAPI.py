# -*- coding: utf-8 -*-

import nltk
import pickle
import json

f = open('./classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

f = open('./word_features.pickle', 'rb')
word_features = pickle.load(f)
f.close()


def extract_features(document):
	global word_features
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

def getSentiment( text):
	text = json.loads( json.dumps([text]))[0]
	return classifier.classify(extract_features(text.split()))



if __name__ == "__main__":
	print "Enter Input"
	while True:
		print getSentiment( raw_input()  ) 
		
