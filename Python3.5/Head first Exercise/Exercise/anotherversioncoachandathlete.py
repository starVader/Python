#!/usr/bin/env python
james = []
julie = []
mikey = []
sarah = []
njames = []
njulie = []
nmikey = []
nsarah = []

def fileopen(filename):
	try:
		with open(filename) as ff:
			data = ff.readline()
		return(data.strip().split(','))
	except IOError as io:
		print ("File error:" + str(io))
		return (None)        


def sanitize(timestring):
    if '-' in timestring:
       splitter = '-' 
    elif ':' in timestring:
        splitter = ':'
    else:
        return(timestring)
    (mins,secs) = timestring.split(splitter)
    return(mins + '.' + secs)
     
sarah = fileopen("sarah.txt")
james = fileopen("james.txt")
mikey = fileopen("mikey.txt")
julie = fileopen("julie.txt")


print sorted(set([sanitize(t) for t in james]))[0:3]
print sorted(set([sanitize(t) for t in mikey]))[0:3]
print sorted(set([sanitize(t) for t in sarah]))[0:3]
print sorted(set([sanitize(t) for t in julie]))[0:3]

