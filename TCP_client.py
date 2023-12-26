import socket


sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = '127.0.0.2'
port = 50000

try:
    sc.connect((address, port))
    print("✈  ✈  ✈   Welcome to aviationstack   ✈  ✈  ✈")
    print(sc.recv(1024).decode('ascii'))
    client_name=input('>>>')
    sc.send(client_name.encode('ascii'))
    while True:
        Options = sc.recv(1024).decode('ascii')
        print(Options)

        option = input("Enter your choice (a, b, c, or d): ")

        if option.lower() == 'c':
            sc.send(option.encode('ascii'))
            ICAO = input('Enter the departure airport ICAO: ')
            sc.send(ICAO.encode())
            print(sc.recv(65000).decode('ascii'))
        elif option.lower() == 'd':
            sc.send(option.encode('ascii'))
            Arrival_IATA = input('Enter Arrival IATA: ')
            sc.send(Arrival_IATA.encode('ascii'))
            print(sc.recv(65000).decode('utf-8'))
        else:
            sc.send(option.encode('ascii'))
            response = sc.recv(65000).decode('ascii')
            print(response)

        exit = input("Do you want to quit?? (y/n): ")
        if exit.lower() == 'y':
            print("Connection has been closed 🔌")
            print("Good Bye")
            break

except ConnectionError as e:
    print(f"Connection error: {e}")
except KeyboardInterrupt:
    print("Client interrupted.")
finally:
    sc.close()