import socket

HOST = 'localhost'
PORT = 4323

# Socket using IPV4 and TCP Protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket
sock.bind((HOST, PORT))


sock.listen()

# WOrking On It....