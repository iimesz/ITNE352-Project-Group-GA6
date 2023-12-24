import socket

#creating a TCP socket :
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# binding the socket : 
adress ='127.0.0.2'
port = 50000
ss.bind((adress, port))




# listen for 3 client :
ss.listen(3)

#accepting the connection
sss, sockname = ss.accept()

# print out the returned values from accept() method
print('Accepted request from', sockname[0] ,'with port number', sockname[1])

#closing the socket :
ss.close()
sss.close()