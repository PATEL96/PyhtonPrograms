from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
Server_Address = ('192.168.0.101', 8080)

server.bind(Server_Address)
server.listen(100)

list_of_connections = []

print("Listening on", Server_Address[1])

while True:
    connection, address = server.accept()
    
    print("Connected From:", address)
    connection.send(bytes("Message Sent.", 'utf-8'))
    data = connection.recv(4096).decode()
    print(data)