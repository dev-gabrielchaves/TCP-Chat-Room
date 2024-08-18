import threading, socket

HOST = "localhost"
PORT = 51251

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message.encode('ascii'))

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            broadcast(message)
        except:
            index = clients.index(client)
            print(f"Error when receiving message from {nicknames[index]}")

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        broadcast(f"{nickname} joined the chat!")

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()