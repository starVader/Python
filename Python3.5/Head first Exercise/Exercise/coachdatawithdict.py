sarah = dict()
temp1 = []
#Sanitizing based in splitter
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            temp1 = data.strip().split(',')# Extract data from file into list
            return ({
                'Name':temp1.pop(0),
                'dob':temp1.pop(0),
                'Times':str(sorted(set([sanitize(t) for t in temp1]))[0:3])})
        # We can return Dictionaries
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

sarah = get_coach_data('sarah.txt')
#print (sarah)
print (sarah['Name'] + "'s fastest times are:" + sarah['Times'])

