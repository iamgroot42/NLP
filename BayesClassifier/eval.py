from SentiAPI import getEntity
import csv
import json

name = raw_input("Enter input file (without .csv ) : ")
f = open("../Input/" + name + ".csv", 'r')
c = csv.reader(f,delimiter=',')
o = open("../Output/" + name + ".csv", 'w')
jso  = open("../Frontend/json/"+name+".json",'w')
print >>o,"S.NO.",",","Entity"
output = []
json_str = "["
i=1

jjjj = []

# Skip header
c.next()

for line in c:
	json_str += "{\"text\": \""
	x = getEntity(line[1])
	#print line[1]," : ",x
	# json_str += line[1].replace("\n"," ").replace("\""," ")+"\",\"val\": \""+x+"\"},"
	jjjj.append( { "text" : line[1] , "val" : x  }  )
	print >>o, i,",",x
	i += 1

json_str += "]"
# print json_str
# jso.write(json_str)


json.dump(jjjj, jso)
o.close()
f.close()
# jso.close()