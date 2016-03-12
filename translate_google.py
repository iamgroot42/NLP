import goslate
import os
import csv

gs = goslate.Goslate()
files_in_dir = os.listdir("Data/Raw/")

for datum in files_in_dir:
	print "Translating " + datum
	o = open("Data/Translated/"+datum,'w')
	g = open("Data/Raw/"+datum,'r')
	f = csv.reader(g, delimiter=',')
	allposts = []
	writer = csv.writer(o)
	for line in f:
		allposts.append(gs.translate(line[0].decode("utf-8"),'hi'))
	allposts = [[row] for row in allposts]
	writer.writerows(allposts)
		# o.write(gs.translate(line,'hi'))
	o.close()
	g.close()

print "Translation complete"