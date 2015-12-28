import socket


#Socket creation

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



#Connect

clientsocket.connect(('localhost',39208))
print clientsocket.recv(1024)


#do something eg: send recv
