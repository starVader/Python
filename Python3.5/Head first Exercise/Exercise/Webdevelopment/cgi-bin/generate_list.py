#! /usr/local/bin/python3
import athletemodel
import yate
import glob


data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)
print (yate.start_response())
print (yate.inlcude_header("Coach kelly's List of Athletes"))
print (yate.start_form("generate_timing_data.py"))
print (yate.para("Select an athlete from the list to work with:"))

for each in athletes:
	print(yate.radio_button("Which_athlete",athletes[each].name))
print (yate.end_form("Select")) 

print (yate.inlcude_footer({"Home": "/index.html"}))
