import goslate
import os
import csv

files_in_dir = os.listdir(path_to_dir)
for file_in_dir in files_in_dir:

gs = goslate.Goslate()

files_in_dir = os.listdir("Data/Raw/")

for datum in files_in_dir:
	f = csv.reader(open("Data/Raw/"+datum), delimiter=",")
	o = open("Data/Translated"+datum,'w')
	for line in f:
		o.write(gr.translate(line,'hi'))
	o.close()
	f.close()

print "Translation complete"