#!/usr/bin/python3
import yate
import cgi
import os
import time
import sys


print(yate.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())
print(host + ", " + addr + ", " + cur_time + ": " + method + ": ",end='', file=sys.stderr)

form = cgi.FieldStorage()
for each in form.keys():
	print(each + '->' + form[each].value,end ='',file=sys.stderr)
print (file=sys.stderr)
print ('OK')
