import socket


sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = '127.0.0.2'
port = 50000

try:
    sc.connect((address, port))
    print("✈️  ✈️  ✈️   Welcome to aviationstack   ✈️  ✈️  ✈️")
    print(sc.recv(1024).decode('ascii'))
    client_name=input('>>>')
    sc.send(client_name.encode('ascii'))
    while True:
        
        Options = sc.recv(1024).decode('ascii')
        print(Options)

        option = input("Enter your choice (a, b, c, or d): ")
        sc.send(option.encode('ascii'))
        

        response = sc.recv(65000).decode('ascii')
        print(response)

        exit = input("Do you want to quit ?? (y/n): ")
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