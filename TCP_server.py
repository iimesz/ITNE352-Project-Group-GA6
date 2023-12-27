import socket
import requests
import json
import threading
import sys

#API 
access_key = 'd7489824234d311924204a18bc9be0b7'
arr_icao=input("Please enter airport code: ")
api_url ='http://api.aviationstack.com/v1/flights'
params_i = {
    'access_key': access_key,
    'arr_icao': arr_icao,
    'limit': 100  
}
response = requests.get(api_url , params=params_i )
data = response.json()

#STORE IN JSON FILE WITH NAME GA6.JSON 
with open('GA6.json', 'w') as f:
        json.dump(data , f , indent=2)
print('The server has been connection with API ✅')

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = '127.0.0.2'
port = 50000
ss.bind((address, port))
print('=' * 20 + '  The server has been started ✔️   ' + '=' * 20)

def handle_clients():
    while True:
        sss, sockname = ss.accept()
        t = threading.Thread(target=option_C, args=(sss, 'name'))
        my_threads.append(t)  

        t.start()

        if ss.fileno() == -1: #check if the socket close 
            print("Socket is closed.")
            break

ss.listen(3)
def option_C(sss,name):
    try:
        sss.send(' ✈️  ✈️  ✈️✈️ Welcome ✈️  ✈️✈️  ✈️  ✈️'.encode('utf-8'))
        client_name = sss.recv(4000).decode('utf-8')
        print('Accepted request from ' + client_name + '\n'+'-'*55 )
        while True:
            option = sss.recv(1).decode('utf-8')
            print('The client  '+ client_name +' is chose the option : '+ option + '\n'+'-'*55 )

            with open('GA6.json', 'r') as r:
                data = json.load(r)

            info =''

            if option.lower() == 'a':
                for i in data['data']:
                    if i["flight_status"] == 'landed':
                        flight_code = i["flight"]["iata"]
                        departure_airport = i["departure"]["airport"]
                        arrival_time = i["arrival"]["actual"]
                        arrival_terminal = i["arrival"]["terminal"]
                        arrival_gate = i["arrival"]["gate"]

                        info += f"Flight IATA Code: {flight_code}\n, Departure Airport: {departure_airport}\n, Arrival Time: {arrival_time}\n, Arrival Terminal: {arrival_terminal}\n, Arrival Gate: {arrival_gate}\n '✈️  ✈️✈️  ✈️  ✈️✈️  ✈️✈️  ✈️  ✈️'\n"
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

                        info += f"Flight IATA Code: {flight_code}\n, Departure Airport: {departure_airport}\n,Departure Time:{departure_time}\n, Departure Delay: {departure_delay}\n, Arrival Time: {arrival_time}\n, Arrival Terminal: {arrival_terminal}\n, Arrival Gate: {arrival_gate}\n'✈️  ✈️✈️  ✈️  ✈️✈️  ✈️✈️  ✈️  ✈️\n'"

                        delayed_flights_exist = True

                if not delayed_flights_exist:
                    info = 'No delayed flights\n'

                sss.sendall(info.encode())

            elif option.lower() == 'c':
                departure_IATA = sss.recv(1024).decode('utf-8')
                departure_IATA = departure_IATA.upper()
                for i in data['data']:
                    if i["departure"]["iata"] == departure_IATA:
                        flight_code = i["flight"]["iata"]
                        departure_airport = i["departure"]["airport"]
                        departure_time = i["departure"]["estimated"]
                        arrival_time = i["arrival"]["estimated"]
                        departure_gate = i["departure"]["gate"]
                        arrival_gate = i["arrival"]["gate"]
                        flight_status = i["flight_status"]
                        info += f"Flight IATA Code: {flight_code}\n, Departure Airport: {departure_airport}\n,Departure Time:{departure_time}\n, arrival time: {arrival_time}\n, Arrival Time: {arrival_time}\n, Departure Gate: {departure_gate}\n, Arrival Gate: {arrival_gate}\n , Flight Status : {flight_status}\n'✈️  ✈️✈️  ✈️  ✈️✈️  ✈️✈️  ✈️  ✈️'\n"
                sss.sendall(info.encode())

            elif option.lower() == 'd':
                Fligth_IATA = sss.recv(1024).decode('utf-8')
                Fligth_IATA = Fligth_IATA.upper()
                for i in data['data']:
                    if i["flight"]["iata"] == Fligth_IATA:
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
                        info += f"Flight IATA Code: {flight_code}\n, Departure Airport: {departure_airport}\n,Departure Gate: {departure_gate}\n, Departure Terminal: {departure_terminal}\n, Arrival Airport: {arrival_airport}\n, Arrival Terminal: {arrival_terminal}\n, Arrival Gate: {arrival_gate}\n, Flight Status : {flight_status}\n, Departure Scheduled: {departure_scheduled}\n, Arrival Scheduled: {arrival_scheduled}\n'✈️  ✈️✈️  ✈️  ✈️✈️  ✈️✈️  ✈️  ✈️'\n"
                sss.sendall(info.encode())
            elif option.lower() == 'q' :
                print(client_name +'  has been disconnected 🔌' + '\n'+'-'*55)
                break 

    except Exception as e:
        print(f"Error in handling client: {e}")
    finally:
        sss.close()
# main thread
my_threads = []
try:
    t = threading.Thread(target=handle_clients)
    t.start()
#accept 3 client and close the server : 
    while True:
        if len(my_threads) >= 5:
            print('    End the server   ')
            break
except KeyboardInterrupt:
    print('Server interrupted. Closing.')   
ss.close()
sys.exit()
