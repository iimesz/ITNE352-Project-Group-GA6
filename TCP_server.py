import socket
import requests
import json


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

#PRINT THE ACCEPTED METHOD
#print('Accepted request from', sockname[0] ,'with port number', sockname[1])

#closing the socket :
#ss.close()
#sss.close()