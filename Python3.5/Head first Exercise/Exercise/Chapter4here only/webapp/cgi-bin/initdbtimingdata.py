import sqlite3

connection = sqlite.connect('coach.sqlite')
cursor = connection.cursor()

import glob

data_files = glob.glob("../data/*.txt")
athletes = athletemodel.put_to_store(data_files)
for each in athletes:
	time = athletes[each].times
	cursor.execute("INSERT INTO timing_data(times) VALUE(?)",(times))
connection.commit()
connection.close()