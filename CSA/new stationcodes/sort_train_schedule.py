#Sort data according to departure time
from operator import itemgetter
L = []
line = []
for _ in xrange(23001):
	line = raw_input().split(' ')
	L.append([(line[0]),(line[1]),(line[2]),(line[3]),(line[4])])
temp = []
temp = sorted(L,key=itemgetter(3))
for item in temp:
	print item[0],item[1],item[2],item[3],item[4]
