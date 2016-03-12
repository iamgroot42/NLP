import nltk
from random import shuffle
from sys import argv
import pickle
from os.path import isfile

argc = len(argv)
if argc != 2 and argc != 3:
	print "Usage\npython senti_stanford.py <<no_of_tweets_for_training>> [<<option>>]"
	print "Options:"
	print "1 : read trained classifier from pickle file"
	print "2 : force redo training and overwrite pickles"
	print "<<no_option>>: looks for pickle file. If not found then train."
	exit(1)

prop = int(argv[1])
if argc == 3:
	opt = int(argv[2])
else:
	opt = -1

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

if opt == -1:
	if isfile('classifier_'+str(prop)+'.pickle'):
		f = open('classifier_'+str(prop)+'.pickle', 'rb')
		classifier = pickle.load(f)
		f.close()
		f = open('word_features_'+str(prop)+'.pickle', 'rb')
		word_features = pickle.load(f)
		f.close()
		
	else:
		pos_tweets = []
		neg_tweets = []
		f = open("train-stanford.csv")
		for k in f.readlines():
			l = k.strip('.\n').split('","')
			pos_tweets.append((l[5],l[0].strip("\"")))
		f.close()

		shuffle(pos_tweets)
		pos_tweets = pos_tweets[:prop]

		def get_words_in_tweets(tweets):
			all_words = []
			for (words, sentiment) in tweets:
				all_words.extend(words)
			return all_words

		def get_word_features(wordlist):
			wordlist = nltk.FreqDist(wordlist)
			word_features = wordlist.keys()
			return word_features

		tweets = []
		for (words, sentiment) in pos_tweets + neg_tweets:
			words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
			tweets.append((words_filtered, sentiment))

		word_features = get_word_features(get_words_in_tweets(tweets))
		training_set = nltk.classify.apply_features(extract_features, tweets)
		classifier = nltk.NaiveBayesClassifier.train(training_set)

		f = open('classifier_'+str(prop)+'.pickle', 'wb')
		pickle.dump(classifier, f)
		f.close()

		f = open('word_features_'+str(prop)+'.pickle', 'wb')
		pickle.dump(word_features, f)
		f.close()
elif opt == 1:
	if isfile('classifier_'+str(prop)+'.pickle'):
		f = open('classifier_'+str(prop)+'.pickle', 'rb')
		classifier = pickle.load(f)
		f.close()
		f = open('word_features_'+str(prop)+'.pickle', 'rb')
		word_features = pickle.load(f)
		f.close()
else:
	pos_tweets = []
	neg_tweets = []
	f = open("train-stanford.csv")
	for k in f.readlines():
		l = k.strip('.\n').split('","')
		pos_tweets.append((l[5],l[0].strip("\"")))
	f.close()

	shuffle(pos_tweets)
	pos_tweets = pos_tweets[:prop]

	def get_words_in_tweets(tweets):
		all_words = []
		for (words, sentiment) in tweets:
			all_words.extend(words)
		return all_words

	def get_word_features(wordlist):
		wordlist = nltk.FreqDist(wordlist)
		word_features = wordlist.keys()
		return word_features

	tweets = []
	for (words, sentiment) in pos_tweets + neg_tweets:
		words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
		tweets.append((words_filtered, sentiment))

	word_features = get_word_features(get_words_in_tweets(tweets))
	training_set = nltk.classify.apply_features(extract_features, tweets)
	classifier = nltk.NaiveBayesClassifier.train(training_set)

	f = open('classifier_'+str(prop)+'.pickle', 'wb')
	pickle.dump(classifier, f)
	f.close()

	f = open('word_features_'+str(prop)+'.pickle', 'wb')
	pickle.dump(word_features, f)
	f.close()

	
test_tweets = []
f = open("test-stanford.csv")
for k in f.readlines():
	l = k.strip('.\n').split('","')
	test_tweets.append((l[5],l[0].strip("\"")))
f.close()

total = len(test_tweets) 
hits = total

for (tweet,sentiment) in test_tweets:
	if classifier.classify(extract_features(tweet.split())) != sentiment:
		hits-=1

print "Accuracy: ",hits*100.0/total,"%"