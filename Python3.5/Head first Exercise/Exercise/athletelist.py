class AthleteList(list): # class inheriting from inbuilt LIST CLASS which already has set of useful functions defined
    def __init__(self,namea,dob =None,times = []):
        list.__init__([]) # initializing the attribute which is itself a class
        self.name = namea
        self.dob = dob
        self.extend(times)
    def top3(self):
        return (sorted(set([sanitize(t)for t in self]))[0:3]) # list comrehension
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = []
        temp1 = data.strip().split(',')
        return AthleteList(temp1.pop(0),temp1.pop(0),temp1)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None) # return NOne because it may cause u need to return something

def sanitize(time_string):
            if '-' in time_string:
                splitter = '-'
            elif ':' in time_string:
                splitter = ':'
            else:
                return(time_string)
            (mins, secs) = time_string.split(splitter)
            return(mins + '.' + secs)


sarah = get_coach_data('sarah.txt')

sarah.append('1.9')
sarah.extend(['1.3','2.7','0.9'])
print (sarah.name + "'s fastest times are:" + str(sarah.top3()))


