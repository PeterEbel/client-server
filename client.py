import socket

# Define server IP and port
server_ip = 'localhost'  # Change this to the server's IP address
server_port = 12345  # Change this to the server's port

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Receive and print the words from the server
received_data = client_socket.recv(1024).decode('utf-8')
print("Received words from the server:")

while received_data:
    print(received_data, end=' ')
    received_data = client_socket.recv(1024).decode('utf-8')

# Close the socket
# client_socket.close()





