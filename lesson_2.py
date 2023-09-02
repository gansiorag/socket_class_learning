import socket
from select import select


HOST = ('localhost', 4875)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(HOST)
server_socket.listen()

to_monitor = []
def accept_connection(server_socket):
        client_socket, addr = server_socket.accept()
        print('Connection from -> ', addr)
        to_monitor.append(client_socket)

        
def send_message(client_socket):
        request = client_socket.recv(4096)
        
        if request:
            print(request)
            response = 'Hello user!!!\n'.encode()
            client_socket.send(response)
        else:
            client_socket.close()
    
def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)
    
    
                
"""
We are bloked answer one client 

creater client - new terminal - nc localhost 4875

if we have several clients, server not answer two client while
first client have connection

"""

if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()