import socket
import requests
import json
import threading
import sys

# access key for API
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
        t1 = threading.Thread(target=client_n, args=(sss,))
        t2 = threading.Thread(target=option_C, args=(sss,))
        my_threads.append(t)
        t1.start()
        t2.start()

        if ss.fileno() == -1:
            print("Socket is closed.")
            break

# Listen for clients
ss.listen()

def client_n(sss):
    sss.send(b'Please enter the client name: ')
    client_name = sss.recv(1024).decode('ascii')
    print('Accepted request from', client_name)

# option a , b, c, d
def option_C(sss):
    try:
        while True:
            sss.send(b"Options:\n"
                    b"a. All arrived flights\n"
                    b"b. All delayed flights\n"
                    b"c. All flights from a specific airport\n"
                    b"d. Details of a particular flight\n"
                    b"Choose an option (a, b, c, or d): ")

            option = sss.recv(1).decode('ascii')

            with open('GA6.json', 'r') as r:
                data = json.load(r)

            info = ''

            if option.lower() == 'a':
                for i in data['data']:
                    if i["flight_status"] == 'landed':
                        flight_code = i["flight"]["iata"]
                        departure_airport = i["departure"]["airport"]
                        arrival_time = i["arrival"]["estimated"]
                        arrival_terminal = i["arrival"]["terminal"]
                        arrival_gate = i["arrival"]["gate"]

                        info += f"Flight IATA Code: {flight_code}, Departure Airport: {departure_airport}, Arrival Time: {arrival_time}, Arrival Terminal: {arrival_terminal}, Arrival Gate: {arrival_gate}\n"
                sss.sendall(info.encode())

            elif option.lower() == 'b':
                delayed_flights_exist = False
                for i in data['data']:
                    D = i['arrival']
                    if D["delay"] is not None:
                        flight_code = i["flight"]["iata"]
                        departure_airport = i["departure"]["airport"]
                        departure_time = i["departure"]["estimated"]
                        arrival_time = D["estimated"]
                        departure_delay = D["delay"]
                        arrival_terminal = D["terminal"]
                        arrival_gate = D["gate"]

                        info += f"Flight IATA Code: {flight_code}, Departure Airport: {departure_airport},Departure Time:{departure_time}, Departure Delay: {departure_delay}, Arrival Time: {arrival_time}, Arrival Terminal: {arrival_terminal}, Arrival Gate: {arrival_gate}\n"

                        delayed_flights_exist = True

                if not delayed_flights_exist:
                    info = 'No delayed flights\n'

                sss.sendall(info.encode())

            elif option.lower() == 'c':
                departure_ICAO = sss.recv(1024).decode('ascii')
                departure_ICAO = departure_ICAO.upper()
                for i in data['data']:
                    if i["departure"]["icao"] == departure_ICAO:
                        flight_code = i["flight"]["iata"]
                        departure_airport = i["departure"]["airport"]
                        departure_time = i["departure"]["estimated"]
                        arrival_time = i["arrival"]["estimated"]
                        departure_gate = i["departure"]["gate"]
                        arrival_gate = i["arrival"]["gate"]
                        flight_status = i["flight_status"]
                        info += f"Flight IATA Code: {flight_code}, Departure Airport: {departure_airport},Departure Time:{departure_time}, arrival time: {arrival_time}, Arrival Time: {arrival_time}, Departure Gate: {departure_gate}, Arrival Gate: {arrival_gate} , Flight Status : {flight_status}\n"
                sss.sendall(info.encode())

            elif option.lower() == 'd':
                Arrival_IATA = sss.recv(1024).decode('ascii')
                Arrival_IATA = Arrival_IATA.upper()
                for i in data['data']:
                    if i["arrival"]["iata"] == Arrival_IATA:
                        flight_code = i["flight"]["iata"]
                        departure_airport = i["departure"]["airport"]
                        departure_gate = i["departure"]["gate"]
                        departure_terminal = i["departure"]["terminal"]
                        arrival_airport = i["arrival"]["airport"]
                        arrival_gate = i["arrival"]["gate"]
                        arrival_terminal = i["arrival"]["terminal"]
                        flight_status = i["flight_status"]
                        departure_scheduled = i["departure"]["scheduled"]
                        arrival_scheduled = i["arrival"]["scheduled"]
                        info += f"Flight IATA Code: {flight_code}, Departure Airport: {departure_airport},Departure Gate: {departure_gate}, Departure Terminal: {departure_terminal}, Arrival Airport: {arrival_airport}, Arrival Terminal: {arrival_terminal}, Arrival Gate: {arrival_gate}, Flight Status : {flight_status}, Departure Scheduled: {departure_scheduled}, Arrival Scheduled: {arrival_scheduled}\n"
                sss.sendall(info.encode())

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
