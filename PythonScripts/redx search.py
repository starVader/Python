# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(raw_input())
for i in range(N):
    mob = str(raw_input())
    match =re.search(r'(^[7-9]\d{9}$',mob)
    if match:
        print "YES"
    else:
        print "NO"
