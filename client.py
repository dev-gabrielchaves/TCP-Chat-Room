import threading, socket

nickname = input("Type your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 51251))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            
            if message == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
            
        except:
            print("An error ocurred!")
            client.close()
            break

def write():
    while True:
        try:
            message = f"{nickname}: {input('')}"
            client.send(message.encode('ascii'))
        except:
            print("An error ocurred!")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()
