# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
mylist = []
result = []
final = [] 
if (1<= N<=5):
    for i in range(N):
        a = raw_input()
        b = float(raw_input())
        mylist = [a,b]
        result.append(mylist)
    result.remove(min(result))
    #print result
    final = min(result)
    result.remove(final)
    min2 = min(result)
    print min2

        
