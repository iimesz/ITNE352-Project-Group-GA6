import socket


#creating the socket:
sc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server :
adress ='127.0.0.2'
port = 50000
sc.connect((adress, port))
print("The request has been sent")

#closing the socket :
sc.close()