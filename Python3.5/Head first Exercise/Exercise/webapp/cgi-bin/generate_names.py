#! /usr/bin/python3

import athletemodel
import yate
import glob
import json

data_files = glob.glob("./data/*.txt")
athletemodel.put_to_store(data_files)
names = athletemodel.get_namesid_from_store()
print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))
