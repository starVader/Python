# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
from dateutil import parser
T = int(raw_input())
for i in range(T):
    date1= str(raw_input())
    date2 = str(raw_input())
    diff = datetime.parser.parse(date1) - datetime.parser.parse(date2)
    print "%d" abs(diff.time_seconds())
