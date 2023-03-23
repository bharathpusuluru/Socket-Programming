import socket
#read
HOST = 'localhost' # Change to IP address of the machine running the server
PORT = 54

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on port {PORT}")

connection, address = server_socket.accept()
print(f"Connected by {address}")

while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    print(f"Received from client: {data}")
    message = input("Enter message to send to client: ")
    print("@Server",message)
    connection.sendall(message.encode())
    if message == "Bye":
        break

connection.close()