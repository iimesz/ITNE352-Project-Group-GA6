import socket
import requests
import json
import threading
import sys



# access code for API
access_key = 'a5a5423540790ed7ad4db33bf14d26e9'

# name of arr_icao
arr_icao=input("Please enter airport code: ")

# API_URL and PARAMS
api_url ='http://api.aviationstack.com/v1/flights'
params_i = {
    'access_key': access_key,
    'arr_icao': arr_icao,
    'limit': 100  
}
#THE RESPONSE AND CONVERT TO JSON
response = requests.get(api_url , params=params_i )

data = response.json()

#STORE IN JSON FILE WITH NAME GA6.JSON 
with open('GA6.json', 'w') as f:
        json.dump(data , f , indent=2)

# creat a TCP socket        
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = '127.0.0.2'
port = 50000
ss.bind((address, port))
print('=' * 20 + '  The server has been started ' + '=' * 20)

# Handle the client :
def handle_clients():
    
    while True:
        
        sss, sockname = ss.accept()
        print('Accepted request from', sockname[0], 'with port number', sockname[1])

        t = threading.Thread(target=option_C, args=(sss,))
        my_threads.append(t)
        t.start()

        if ss.fileno() == -1:
            print("Socket is closed.")
            break

# Listen for clients
ss.listen()

# option a , b, c, d
def option_C(sss):
    try:
        while True :
            
            sss.send(b"Options:\n"
                    b"a. All arrived flights\n"
                    b"b. All delayed flights\n"
                    b"c. All flights from a specific airport\n"
                    b"d. Details of a particular flight\n"
                    b"Choose an option (a, b, c, or d): ")

            option = sss.recv(1).decode('ascii')

            with open('GA6.json', 'r') as file:
                data = json.load(file)
            listt = ''

            if option.lower() == 'a':
                
                for i in range(len(data['data'])):
                    D = data['data'][i]['arrival']
                    listt += '#{}: flight IATA code: {} \ndeparture airport name: {} \narrival time: {} \narrival terminal number: {} \narrival gate: {}'.format(
                        i, D['icao'], D['airport'], D['scheduled'], D['terminal'], D['gate'])
                    listt += '\n'
                sss.sendall(listt.encode())

            if option.lower() == 'b':
                delayed_flights_exist = False
                for i in range(len(data['data'])):
                    D = data['data'][i]['departure']
                    if D["delay"] != None:
                        listt += '#{}: flight IATA code: {} \ndeparture airport name: {} \narrival time: {} \ndelay:  {} \narrival terminal number: {} \narrival gate: {}'.format(
                            i, D['icao'], D['airport'], D['scheduled'], D["delay"], D['terminal'], D['gate'])
                        listt += '\n'
                        delayed_flights_exist = True

                if not delayed_flights_exist:
                    listt = 'No delayed flights\n'
                
                sss.sendall(listt.encode())
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        sss.close()

     

# threading 
my_threads = []

try:
    t = threading.Thread(target=handle_clients)
    t.start()

    while True:
        if len(my_threads) >= 5:
            print('End the server')
            break
            

except KeyboardInterrupt:
    print('Server interrupted. Closing.')


ss.close()
sys.exit()