import sys
temp1 = []
f = open("withtra_bu_pl.txt","r")
#print f
#count = 0
for line in f:
	a = line.split(' ')
	#print 'adapaavi'
	x = int(a[3]) + 48*60*60
	y = int(a[4]) + 48*60*60
	#if x > y :
		#y += 24*60*60
	#	count += 1
	a[3] = str(x)
	a[4] = str(y)
	z = a[5];
	a[5] = z[:-1]
	temp1.append(a)

#print temp1
#print count
#sys.exit(0)
for x in temp1:
	#print 'yolo'
	#if x[0] == ' ':
	#	continue
	print x[0],x[1],x[2],x[3],x[4],x[5]