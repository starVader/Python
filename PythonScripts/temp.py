# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
mylist = []
if (2 <= N <= 10):
    temp = raw_input()
    mylist = temp.split()
    last = []
    for i in mylist:
        if ((i not in last) or(-100 <=i <= 100)):
            last.append(i)

    length = len(last)
    last = list(map(int, last))# convert strings to int
    last.sort()
    print last[length - 2]
        
        

                                   
        
        

    
