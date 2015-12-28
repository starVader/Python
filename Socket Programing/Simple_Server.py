
import socket


#Creting a socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Binding to port and host here localhost otherwise socket.gethostname()
serversocket.bind(('localhost',39208))

#Start listening with a queue size
serversocket.listen(5)


#Server loop

while 1:
    #accept
    (clientsocket,address) = serversocket.accept()
    if clientsocket:
        print "A Client Connected"

    clientsocket.send("Thanks for connecting Client")
    clinetsocket.close()
    #do something eg: send recv
