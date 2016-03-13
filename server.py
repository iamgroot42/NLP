import csv
import json
import SentiAPI

handle = raw_input()

f = open("Data/Raw/" + handle + "_tweets.csv",'r')
x = csv.reader(f, delimiter=',')

data = []
i=0
for y in x:
	# print y[0]
	temp = {"text":y[0], "val":SentiAPI.getSentiment(y[0])}
	data.append(temp)
	print temp['text'] + " =+> " +temp['val']

	if i == 50:
		break
	i += 1

print len(data)

with open("Data/analyzed/" + handle + ".json"  , 'w') as outfile:
	json.dump(data, outfile)
