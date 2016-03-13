# -*- encoding: utf-8 -*-
import string
import json
import glob

f = open("../Data/unformatted_ground_truth/hindi_mov_reviews.txt")
formatted = []

for k in f.readlines():
	l = k.strip('.\n').split(' ')
	if k[0] == '1':
		formatted.append({ "text" : ' '.join(l[1:]), "val" : 'positive'})
	elif k[0] == '0':
		formatted.append({ "text" : ' '.join(l[1:]) , "val" : 'negative'})



with open("../Data/formatted_groundtruth/hindi_mov_reviews.json"  , 'w') as outfile:
	json.dump(formatted, outfile)


f = open("../Data/unformatted_ground_truth/tweet_pos_hin.txt")
formatted = []

for k in f.readlines():
	l = k.replace('", "' , '","' ).replace('" "' , '","' )
	l = k.strip('.\n').split('"')
	tex = l[-2]
	if( len(tex) > 7 ):
		formatted.append({ "text" : tex , "val" : 'positive'})


with open("../Data/formatted_groundtruth/tweet_pos_hin.json"  , 'w') as outfile:
	json.dump(formatted, outfile)


f = open("../Data/unformatted_ground_truth/tweet_neg_hin.txt")
formatted = []

for k in f.readlines():
	l = k.replace('", "' , '","' ).replace('" "' , '","' )
	l = k.strip('.\n').split('"')
	tex = l[-2]
	if( len(tex) > 7 ):
		formatted.append({ "text" : tex , "val" : 'negative'})


with open("../Data/formatted_groundtruth/tweet_neg_hin.json"  , 'w') as outfile:
	json.dump(formatted, outfile)


# now prep the emoje data
files = glob.glob('../Data/emoji_tweets/*.json')
formatted = []

for f in files:
	with open(f) as data_file:    
		data = json.load(data_file)

		for d in data:
			d = d.replace("\n" , " ")
			if (":)" in d ) or ( ":-)" in d):
				d = d.replace(":)" , "")
				d = d.lower()
				d = "".join([c for c in d if c in string.letters or c in string.whitespace])
				formatted.append({ "text" : d , "val" : 'positive'})
			elif (":(" in d ) or ( ":/" in d):
				d = d.replace(":(" , "")
				d = d.lower()
				d = "".join([c for c in d if c in string.letters or c in string.whitespace])
				formatted.append({ "text" : d , "val" : 'negative'})


with open("../Data/formatted_groundtruth/tweet_from_emojis.json"  , 'w') as outfile:
	json.dump(formatted, outfile)




for x in ['tweet_from_emojis' ]:

	with open("../Data/formatted_groundtruth/"+x+".json") as data_file:    
		data = json.load(data_file)
		for l in data:
			print l['text'] + " =+> " + l['val']



