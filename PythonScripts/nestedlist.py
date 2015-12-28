# Enter your code here. Read input from STDIN. Print output to STDOUT
def getkey(item):
    return item[1]

N = int(raw_input())
mylist = []
result = []
if (1<= N<=5):
    for i in range(N):
        a = raw_input()
        b = float(raw_input())
        mylist = [a,b]
        result.append(mylist)

sorted(result, key=getkey)
print result
flist = []
sec_lar = result[0]
num = sec_lar[1]
for name,mark in result:
    if (mark > num):
        num = mark
        flist = [name,mark]
        break
for name,mark in result:
    if (mark == num):
        flist.append([name,mark])
print flist
        
    
