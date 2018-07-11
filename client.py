import socket
import time
name = socket.gethostname()
print 'Client Name:',name
clientIP = socket.gethostbyname(name)
print 'Client IP Address:', clientIP

while True:
    client = socket.socket()  #Creating a socket at client to connect the server
    #With the help of this socket at client, client will try to connect the server
    client.connect(('192.168.0.108',1559)) #IP address of server
    client.send('Hello Prasad!')  #Client will send the data to server after every 5 sec
    print 'Data sent!'
    serverData = client.recv(1024)
    print 'Data from server:', serverData
    time.sleep(5)
