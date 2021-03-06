import sys

from array import *

MAX = 2**24 - 1 
NO_OF_STATIONS = 2265 #max number of stations
no_of_connections = 178665 #no of input connections
class Connections:
	def __init__(self,line):
			parameters = line.split(' ');

			self.train_no = parameters[0]
			self.dept_stn = int(parameters[1])
			self.arr_stn  = int(parameters[2])
			self.dep_time = int(parameters[3])
			self.arr_time = int(parameters[4])
			temp = parameters[5]
			self.label = temp[:-1]

def TimeTable1(connections):
	#connections = []
	f = open("withtra_bu_pl.txt","r")
	for line in f:
		connections.append(Connections(line))
		#print line[:-1]
	f.close()
	return;

def TimeTable2(connections):
	#connections = []
	f = open("withtra_bu_pl_2.txt","r")
	for line in f:
		connections.append(Connections(line))
		#print line[:-1]
	f.close()
	return;

def TimeTable3(connections):
	#connections = []
	f = open("withtra_bu_pl_3.txt","r")
	for line in f:
		connections.append(Connections(line))
		#print line[:-1]
	f.close()
	return;

if len(sys.argv) != 3:
	print 'Format is python CSA_v3.py <Source> <Destination>'
#Station codes
Station_Code = {}
f = open("Stations.txt","r")
for line in f:
	y = line[:-1].split(" ")
	str1 = ""
	for x in y[1:]:
		str1 += " " + x
	Station_Code[int(y[0])] = str1
	#print int(y[0]),str1
#for key,value in Station_Code.iteritems():
	#print key,value
f.close()

#Program execution starts here
connections = []
TimeTable1(connections)
TimeTable2(connections)
TimeTable3(connections)

#for x in connections:
#	print x.train_no,x.dept_stn,x.arr_stn,x.dep_time,x.arr_time
Incoming_Connection = array('I') #Best Incoming connection as unsigned integer
Earliest_Arrival = array('I') #Arrival timestamp as unsigned integer
#Departure_Station = "Madgaon"
Departure_Station = int(sys.argv[1])
Start = Station_Code[int(Departure_Station)]

#Arrival_Station = "Bangarapet"
#sys.exit()
Arrival_Station = int(sys.argv[2])
End = Station_Code[int(Arrival_Station)]

#Departure_Station = raw_input("Enter Departure Station name : ")

#for k,v in Station_Code.iteritems():
#	if v[1:] == Departure_Station:
#        	Departure_Station = k
#        	print 'Station found'
#        	break

#Arrival_Station = raw_input("Enter Arrival Station name : ")
#for k,v in Station_Code.iteritems():
#    if v[1:] == Arrival_Station:
#        Arrival_Station = k
#        print 'Station found'
#        break

#temp = (raw_input("Enter Departure Time: ").split(":"))
#Departure_Time = int(temp[0])*3600 + int(temp[1])*60

Departure_Time = 8*60*60

#flight_mode = raw_input("Type 'True' if you wanna travel by flight : ")
#train_mode = raw_input("Type 'True' if you wanna travel by train : ")
#bus_mode = raw_input("Type 'True' if you wanna travel by bus : ")
flight_mode = 'True'
train_mode = 'True'
bus_mode = 'True'


preferred_modes = []
if flight_mode == 'True':
	#print 'Yes Flight'
	preferred_modes.append('flight')
if train_mode == 'True':
	#print 'Yes Train'
	preferred_modes.append('train')
if bus_mode == 'True':
	#print 'Yes Bus'
	preferred_modes.append('bus')



#Departure_Time = 11*60*60
print '------------------------------------------------------------------------'
print 'Query:',Start,'to',End
print 'Departure Time: 08:00'
print 'Modes preferred',preferred_modes
#sys.exit(0)

print "**Schedule**"

#CSA Starts here
Incoming_Connection = array('I', [MAX for _ in xrange(no_of_connections)])
Earliest_Arrival = array('I', [MAX for _ in xrange(no_of_connections)])

Earliest_Arrival[Departure_Station] = Departure_Time

Min_Arrival = MAX 
first_time = 0
for i,j in enumerate(connections):
	#print Earliest_Arrival[1300]
	if j.arr_time < Earliest_Arrival[j.arr_stn] and j.dep_time >= Earliest_Arrival[j.dept_stn]:
		if j.label not in preferred_modes:
			continue
		if first_time == 0: first_time = i
		Earliest_Arrival[j.arr_stn] = j.arr_time
		Incoming_Connection[j.arr_stn] = i

		if j.arr_stn == Arrival_Station:
			Min_Arrival = min(Min_Arrival, j.arr_time)
	elif j.arr_time > Min_Arrival:
		break
	elif (first_time + 2*len(connections)) == i + 1:
		break

if Incoming_Connection[Arrival_Station] == MAX :
	print "NO TRAINS AVAILABLE STARTING THE SAME DAY"
else:
	Route = []
	#Do Backtracking
	prev_connection = Incoming_Connection[Arrival_Station]
	i = 2
	while prev_connection != MAX:
		c = connections[prev_connection]
		Route.append(c)
		#print c.train_no,c.dep_time,c.arr_time,c.dept_stn,c.arr_stn,c.label
		if c.dept_stn == Departure_Station: break
		prev_connection = Incoming_Connection[c.dept_stn]
		#print 'Out here'
	#Printing Route
	for x in reversed(Route):
		while x.dep_time >= 86400:
			x.dep_time = x.dep_time % 86400

		while x.arr_time >= 86400:
			x.arr_time = x.arr_time % 86400

		hr1,min1 = x.dep_time/3600,(x.dep_time - (x.dep_time/3600)*3600)/60
		if hr1 < 10: hr1 = '0'+str(hr1)
		if min1 < 10: min1 = '0'+str(min1)
		
		hr2,min2 = x.arr_time/3600,(x.arr_time - (x.arr_time/3600)*3600)/60
		if hr2 < 10: hr2 = '0'+str(hr2)
		if min2 < 10: min2 = '0'+str(min2)

		print "{} {} to {} {}:{} {}:{} {}".format(x.train_no,Station_Code[x.dept_stn],Station_Code[x.arr_stn],hr1,min1,hr2,min2,x.label)

print "Done"
		
			

