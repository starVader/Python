class AthleteList(list):
    def __init__(self,namea,dob =None,times = []):
        list.__init__([])
        self.name = namea
        self.dob = dob
        self.extend(times)
    def top3(self):
        return (sorted(set([sanitize(t)for t in self]))[0:3])

def sanitize(timestring):
    if '-' in timestring:
       splitter = '-' 
    elif ':' in timestring:
        splitter = ':'
    else:
        return(timestring)
    (mins,secs) = timestring.split(splitter)
    return(mins + '.' + secs)



sarah = AthleteList('Sarah Sweeney')

print (sarah.name)
sarah.append('3.5')
sarah.extend(['3.4','1-3'])
print (sarah.top3())



