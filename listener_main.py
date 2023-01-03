'''Run continuously and receive UDP data on port 50200'''

import socket
import datetime
import process_data

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 50200))

while True:
    data = sock.recv(256) # blocking till data received
    
    print('\n')
    print(datetime.datetime.now()) 
    print('data receiveds')

    try:
        data = data.decode().strip()
    except: # issue decoding
        print('error while decoding')
        print('---DATA---')
        print(data)
        print('---END---')
        continue
    
    print('data decoded')
    print('---DATA---')
    print(data)
    print('---END---')

    process_data.main(data) # act on content of message
