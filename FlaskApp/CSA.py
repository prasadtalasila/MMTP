import sys

from array import *
from flask import Flask, render_template
from flask import Flask
from flask import request
from flask import render_template,jsonify

import sys

from array import *

#temp=("00:00".split(":"))
#Arrival_Station=""
#Departure_Station=""
#Arr_Station=0
#Dep_Station=0
MAX = 2**24 - 1 
NO_OF_STATIONS = 2000 #max number of stations
no_of_connections = 8281 #no of input connections

class Connections:
    def __init__(self,line):
        parameters = line.split(" ");

        self.train_no = int(parameters[0])
        self.dept_stn = int(parameters[1])
        self.arr_stn  = int(parameters[2])
        self.dep_time = int(parameters[3])
        self.arr_time = int(parameters[4])

def TimeTable(connections):
    	#connections = []
    #t=0
    f = open("Sorted_Schedule.txt","r")
    for line in f:
        #t=t+1
        #print t
        connections.append(Connections(line[:-1]))
        #print line[:-1]
    f.close()
    return;


app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/', methods=['POST'])
def my_form_post():

    temp = request.form['d_time'].split(":")	
    Arrival_Station=request.form['dest']
    Departure_Station=request.form['src']
    #print temp[0]
    #print Arrival_Station
    #print Departure_Station
    
    
    

#Station codes
    Station_Code = {}
    f = open("Station_Code.txt","r")
    for line in f:
        y = line[:-1].split(" ")
        str1 = ""
        for x in y[1:]:
            str1 += " " + x
        Station_Code[int(y[0])] = str1
	    #print int(y[0]),str1
    #for key,value in Station_Code.iteritems():
     #   print key,value
    f.close()

#Program execution starts here
    connections = []
    TimeTable(connections)
        
    Incoming_Connection = array('I') #Best Incoming connection as unsigned integer
    Earliest_Arrival = array('I') #Arrival timestamp as unsigned integer
    #Departure_Station = "Bangarapet"
    #Departure_Station = raw_input("Enter Departure Station name : ")

    for k,v in Station_Code.iteritems():
        if v[1:] == Departure_Station:
            Departure_Station = k
            #print "DEP K"	
            break

    for k,v in Station_Code.iteritems():
        if v[1:] == Arrival_Station:
            Arrival_Station = k
            #print "ARR K"
            break

    #temp = (raw_input("Enter Departure Time: ").split(":"))
    Departure_Time = int(temp[0])*3600 + int(temp[1])*60

    print "**Schedule**"

    #CSA Starts here
    Incoming_Connection = array('I', [MAX for _ in xrange(no_of_connections)])
    Earliest_Arrival = array('I', [MAX for _ in xrange(no_of_connections)])
    
    Earliest_Arrival[Departure_Station] = Departure_Time
    #Earliest_Arrival[0] = Departure_Time
    Min_Arrival = MAX 
    #print "HERE"
    #y=0
    for i,j in enumerate(connections):
        #y=y+1
        #print y
    	#print Earliest_Arrival[1300]
        if j.dep_time >= Earliest_Arrival[j.dept_stn] and j.arr_time < Earliest_Arrival[j.arr_stn]:
            Earliest_Arrival[j.arr_stn] = j.arr_time
            Incoming_Connection[j.arr_stn] = i

            if j.arr_stn == Arrival_Station:
                Min_Arrival = min(Min_Arrival, j.arr_time)
        elif j.arr_time > Min_Arrival:
            break
    #print "AHA"  
    lis=['SCHEDULE']      
    #print Incoming_Connection[Arrival_Station]
    if Incoming_Connection[Arrival_Station] == MAX :
        print "NO TRAINS AVAILABLE"

    else:
        Route = []
	#Do Backtracking
	prev_connection = Incoming_Connection[Arrival_Station]
	#prev_connection = Incoming_Connection[0]

	while prev_connection != MAX:
            c = connections[prev_connection]
            Route.append(c)
            prev_connection = Incoming_Connection[c.dept_stn]

	#Printing Route
	for x in reversed(Route):
            hr1,min1 = x.dep_time/3600,(x.dep_time - (x.dep_time/3600)*3600)/60
            hr2,min2 = x.arr_time/3600,(x.arr_time - (x.arr_time/3600)*3600)/60
            lis.append("{} {} to {} {}:{} {}:{}".format(x.train_no,Station_Code[x.dept_stn],Station_Code[x.arr_stn],hr1,min1,hr2,min2))
            print "{} {} to {} {}:{} {}:{}".format(x.train_no,Station_Code[x.dept_stn],Station_Code[x.arr_stn],hr1,min1,hr2,min2)

    print "Done"
    return jsonify(results=lis)
		

if __name__ == '__main__':
  app.run(debug=True)
		

