import socket


sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = '127.0.0.2'
port = 50000
<<<<<<< HEAD

try:
    sc.connect((address, port))
    print("✈️  ✈️  ✈️   Welcome to aviationstack   ✈️  ✈️  ✈️")

    while True:
        menu = sc.recv(1024).decode('ascii')
        print(menu)

        option = input("Enter your choice (a, b, c, or d): ")
        sc.send(option.encode('ascii'))

        response = sc.recv(65000).decode('ascii')
        print(response)

        quit = input("Do you want to QUIT (y/n): ")
        if quit.lower() == 'y':
            print("Connection has been closed 🔌")
            print("Good Bye")
            break

except ConnectionError as e:
    print(f"Connection error: {e}")
except KeyboardInterrupt:
    print("Client interrupted.")
finally:
    sc.close()
=======
sc.connect((adress, port))
print("✈  ✈  ✈   Welcome to aviationstack   ✈  ✈  ✈")


try:
    while True:
        menu = sc.recv(1024).decode('ascii')
        print(menu)

        # Choose an option
        option = input("Enter your choice (a, b, c, or d): ")
        sc.send(option.encode('ascii'))
        if option == 'a':
            IATA= input(' Enter The IATA code')
            sc.send(IATA.encode('ascii'))
            response= response = sc.recv(1024).decode('ascii')

        #response = sc.recv(1024).decode('ascii')
        #print(response)

    
        another_request = input("Do you want to make another request? (y/n): ")
        if another_request.lower() != 'y':
            print(' Thank you ')
            break
        

except KeyboardInterrupt:
    pass
finally:
    sc.close()







#print(sc.recv(1024).decode('ascii'))
#arr_iaco=input('>>>')
#sc.send(arr_iaco.encode('ascii'))
#print(sc.recv(1024).decode('ascii'))



#closing the socket :
sc.close()
>>>>>>> 42247b14027f17990659c6f23f583a5a76e83574
