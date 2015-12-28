# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
dd,mm,yy = map(int,raw_input().split())
cal = calendar.weekday(yy,mm,dd)
if cal == 0:
    print "MONDAY"
if cal == 6:
    print "SUNDAY"
elif cal == 1:
    print "TUESDAY"
elif cal == 2:
    print "WEDNESDAY"
elif cal == 3:
    print "THURSDAY"
elif cal == 4:
    print "FRIDAY"
elif cal == 5:
    print "SATURDAY"
