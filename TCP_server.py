import socket
import requests
import json


# Replace 'YOUR_ACCESS_KEY' with your actual aviationstack API key
access_key = 'a5a5423540790ed7ad4db33bf14d26e9'

# Replace 'YOUR_AIRPORT_CODE' with the airport code you are interested in
arr_icao=input("Please enter airport code: ")

# Aviationstack API endpoint for flights at a specific airport
api_url ='http://api.aviationstack.com/v1/flights'
params_i = {
    'access_key': access_key,
    'arr_icao': arr_icao,
    'limit': 100  
}
# Make a GET request to the aviationstack API
response = requests.get(api_url , params=params_i )

data = response.json()

# Store the retrieved data in a JSON file
with open('GA6.json', 'w') as f:
        json.dump(data , f , indent=2)

        print("Data saved to GA6.json")


#creating a TCP socket :
#ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# binding the socket : 
#adress ='127.0.0.2'
#port = 50000
#ss.bind((adress, port))

# listen for 3 client :
#ss.listen(3)

#accepting the connection
#sss, sockname = ss.accept()

# print out the returned values from accept() method
#print('Accepted request from', sockname[0] ,'with port number', sockname[1])

#closing the socket :
#ss.close()
#sss.close()