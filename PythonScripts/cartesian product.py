# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
list1 = map(int ,raw_input().split())
list2 = map(int, raw_input().split())
result = list(product(list1,list2))
print (' '.join(map(str,result))) # print list without , and []
