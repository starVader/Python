x = int(raw_input())
y = int(raw_input())
z = int(raw_input())

N = int(raw_input())
final = []
mylist = [i for i in range(N)]

#cuboid = [x, y, z]
xpossible = [i for i in range(x)]
xpossible.append(x)
ypossible = [i for i in range(y)]
ypossible.append(y)
zpossible = [i for i in range(z)]
zpossible.append(z)
#print xpossible
#print ypossible
#print zpossible
flist = []
tlist = []
#for a in mylist:
for b in xpossible:
     for c in ypossible:
         for d in zpossible:
             #print d,b,c,a
              if(b+c+d != N):
                   flist.append([b,c,d])
                    #print flist
print flist
