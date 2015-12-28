import pickle
man = []
other = []

try:
    with open('sketch.txt') as data: 

        for eachline in data:
            try:
                (role,line_spoken) = eachline.split(':',1)
                line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
    
except IOError as Io:
    print ('File error:' +str(Io))
try:
    with open('mandata.txt', 'wb') as man_file, open('otherdata.txt', 'wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as pe:
    print("Pickle error:" +str(pe))

try:
    with open('mandata.txt','rb') as manfile:
        mlist = pickle.load(manfile)
        print(mlist)
except IOError as io:
    print('File error:' +str(io))
