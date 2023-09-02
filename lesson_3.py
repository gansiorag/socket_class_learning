import socket
import selectors

selector = selectors.DefaultSelector()

def server():
    HOST = ('localhost', 4875)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(HOST)
    server_socket.listen()
    
    selector.register(fileobj = server_socket, events = selectors.EVENT_READ, data = accept_connection)



def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from -> ', addr)
    selector.register(fileobj = client_socket, events = selectors.EVENT_READ, data = send_message)

        
def send_message(client_socket):
        request = client_socket.recv(4096)
        
        if request:
            print(request)
            response = 'Hello user!!!\n'.encode()
            client_socket.send(response)
        else:
            selectors.unregister(client_socket)
            client_socket.close()
    
def event_loop():
    while True:
        events = selector.select() # {key, events
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)
    
    
                
"""
We are bloked answer one client 

creater client - new terminal - nc localhost 4875

if we have several clients, server not answer two client while
first client have connection

"""

if __name__ == '__main__':
    server()
    event_loop()