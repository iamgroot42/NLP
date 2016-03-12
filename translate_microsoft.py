import os
import csv
from mstranslator import Translator

CLIENT_ID = 'NLP'
CLIENT_SECRET = '7I2PWW9SJDRNj72bIjTqh7xOn7eke+rPNDx94JUKJEA='


translator = Translator('NLP', CLIENT_SECRET)
files_in_dir = os.listdir("Data/Raw/")

for datum in files_in_dir:
	print "Translating " + datum
	o = open("Data/Translated/"+datum,'w')
	g = open("Data/Raw/"+datum,'r')
	f = csv.reader(g, delimiter=',')
	allposts = []
	writer = csv.writer(o)
	for line in f:
		allposts.append(translator.translate(line[0].decode("utf-8"), lang_from='hi', lang_to='en'))
	allposts = [[row] for row in allposts]
	writer.writerows(allposts)
		# o.write(gs.translate(line,'hi'))
	o.close()
	g.close()

print "Translation complete"