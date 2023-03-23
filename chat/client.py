import socket

HOST = 'localhost' 
PORT = 54

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter message to send to server: ")
    print("@client:",message)
    client_socket.sendall(message.encode())
    if message == "Bye":
        break
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Received from server: {data}")

client_socket.close()