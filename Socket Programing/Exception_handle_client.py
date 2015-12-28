import socket

host = 'localhost'
Port = 39208

try:
   csock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
   print msg

try :
    csock.connect((host,Port))
except socket.error as msg:
    print msg
    print "Closing socket"
    csock.close()
print csock.recv(1024)
csock.send("I ma fine")

