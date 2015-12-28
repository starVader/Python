#! /usr/bin/python3

import yate
import cgi
import athletemodel
import athletelist


# CGI Error Checking 
import cgitb		#
cgitb.enable()		#
					#
#CGI error checking

#print ("Foo bar")
form_data = cgi.FieldStorage()
#print ("Hello")
athlete_name = form_data['Which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)
print (yate.start_response())
print (yate.include_header("Coach kelly's Timing of Athletes"))
print (yate.header("Athlete: " + athlete['Name'] + "DOB" + athlete['dob'] ))
print (yate.para("Timing data for" + athlete_name + ':'))

print (yate.u_list(athlete['top3']))
print (yate.para("The Entire set of timing data is :" + str(athlete['data']) + "Duplicates removed") 

print (yate.include_footer({"Home": "/index.html" ,"Select another Athlete": "generate_list.py"}))
