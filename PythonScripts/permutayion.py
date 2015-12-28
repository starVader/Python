# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S,K = raw_input().split()
K = int(K)
mystr =''
result =[]
if(S.isupper()) & (0 <K <= len(S)):
        mylist = list(permutations(S,K))
        for i in mylist:
            mystr = i[0]+i[1]
            result.append(mystr)
        result.sort()
        for i in result:
            print i
