import pickle
from athletelist import AthleteList


def get_coach_data(filename):
   try:
        with open(filename) as f:
            data = f.readline()
        temp1 = []
        temp1 = data.strip().split(',')
        return AthleteList(temp1.pop(0),temp1.pop(0),temp1)
   except IOError as ioerr:
        print('File error:in get coach' + str(ioerr))
 
def put_to_store(files_list):
    all_athletes = {}
    for each in files_list:
      obj = get_coach_data(each)
      all_athletes[obj.name] = obj
    try:
      with open ('athletedata.txt','wb') as athd:
         pickle.dump(all_athletes,athd)
    except IOError as ioerr:
      print ("File error in put_to_store:" + str(ioerr))
    except pickle.PickleError as pe:
      print ("Pickle error:" + str(pe))
    return (all_athletes)

def get_from_store():
   all_athletes = {}
   try:
      with open('athletedata.txt','rb') as athd:
         all_athletes = pickle.load(athd)
   except IOError as ioerr:
      print("File error: in get_from_store" + str(ioerr))
   except pickle.PickleError as pe:
      print ("Pickle error:" + str(pe))
   return (all_athletes)

                     
