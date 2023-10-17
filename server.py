import socket
import time

# Define server IP and port
server_ip = 'localhost'  # Change this to your server's IP address
server_port = 12345  # Change this to your desired port number

# Create a socket and bind it to the server IP and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)  # Listen for a single client connection

print(f"Server listening on {server_ip}:{server_port}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Read and send words from the text file to the client
with open('/home/peter/Projects/spark/data/bibel.txt', 'r') as file:
    content = file.read()
    client_socket.send(content.encode())
    words = content.split(' ')

for word in words:
    client_socket.send(word.encode())
    time.sleep(10)

# Close the sockets

client_socket.close()
server_socket.close()

