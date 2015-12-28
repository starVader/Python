import sys
def print_lol(the_list, indent=False, level=0,Ifile= sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1,Ifile)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='',file =Ifile )
            print(each_item, file =Ifile)
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

print ("Success1")

try:
    with open("mandata.txt","w") as out:
        print_lol(man,False,0,out)
    with open("othermandata.txt","w") as out1:
        print_lol(other,False,0,out1)
except IOError as Io:
    print("File error:" + str(Io))

print ("Success2")





