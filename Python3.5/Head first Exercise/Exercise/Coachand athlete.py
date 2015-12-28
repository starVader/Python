james = []
julie = []
mikey = []
sarah = []

def extract(alist,fi):
    for each in fi:
        alist.append(each)
    print (sorted(alist))

try:
    with open('james.txt','r') as jam,open('julie.txt','r') as jul,open('mikey.txt','r') as mik, open('sarah.txt','r') as sar:
        extract(james,jam)
        extract(sarah,sar)
        extract(julie,jul)
        extract(mikey,mik)
except IOError as io:
    print('File error:'+str(io))


