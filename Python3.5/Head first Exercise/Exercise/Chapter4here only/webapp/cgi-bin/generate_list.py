#! /usr/bin/python3
import athletemodel
import yate
import initdbathletes



#print ('Hi')
data_files = glob.glob("./data/*.txt")
#print ('Foo')
athletes = athletemodel.get_namesid_from_store(data_files)
#print ('Bar')
#print athletes
print (yate.start_response())
print (yate.include_header("NUAC's List of Athletes"))
print (yate.start_form("generate_timing_data.py"))
print (yate.para("Select an athlete from the list to work with:"))

for each in athletes:
	print(yate.radio_button_id("Which_athlete",each[0],each[1]))
print (yate.end_form("Select")) 

print (yate.include_footer({"Home": "/index.html", "Get Athlete Names": "/cgi-bin/generate_names.py"}))
