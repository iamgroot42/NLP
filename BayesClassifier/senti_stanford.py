import nltk
from sys import argv
pos_tweets = []
neg_tweets = []
f = open("train-stanford.csv")
prop = int(argv[1])
for k in f.readlines()[:prop]:
	l = k.strip('.\n').split('","')
	pos_tweets.append((l[5],l[0].strip("\"")))
f.close()

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