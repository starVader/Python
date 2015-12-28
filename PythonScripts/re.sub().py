import re
N = int(raw_input())
for i in range(N):
    string = str(raw_input())
    string = re.sub("&&{2}","and",string)
    print string
