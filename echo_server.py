import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    # initiate port no above 1024
    port = 12345
    # get a socket instance
    server_socket = socket.socket()
    # bind host address and port together
    server_socket.bind((host, port))
    print("Server listening at " + host + ":" + str(port))
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    # accept new connection
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("Received from Client: " + str(data))
        data = input(' -> ')
        # send data to the client
        conn.send(data.encode())

    # close the connection
    conn.close()


if __name__ == '__main__':
    server_program()
