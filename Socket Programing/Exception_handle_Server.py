import socket

host = 'localhost'
Port = 39208

try:
   sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
   print msg

try:
   sock.bind((host, Port))
except socket.error as msg:
  print msg
  sock.close()
    
try:
  sock.listen(5)
except socket.error as msg:
  print msg
  sock.close()

if sock is not None:
    print "Server listening on Port %d"%Port

conn,addr = sock.accept()
print "Client connected to ",addr
while 1:
    sdata = "How are You ? "
    conn.send(sdata)
    print conn.recv(1024)
    
conn.close()
    
