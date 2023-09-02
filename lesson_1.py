import socket


HOST = ('localhost', 4875)
socket_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_socket.bind(HOST)
socket_socket.listen()
print('I am listening yuor connection !!!')

while True:
    print('start accept')
    client_socket, addr = socket_socket.accept()
    print('Connection -> ', addr)
    while True:
        request = client_socket.recv(4096)
        
        if not request:
            break
        else:
            response = 'Hello user!!!\n'.encode()
            client_socket.send(response)
            
"""
We are bloked answer one client 

creater client - new terminal - nc localhost 4875

if we have several clients, server not answer two client while
first client have connection

"""
            

