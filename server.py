import socket, threading, pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5558
SERVER = socket.gethostbyname(socket.gethostname())
s.bind((SERVER, PORT))
print("Welcome to chat-server")

users = []

def client(client_socket, addr, USER):
    while True:
        try:
            msg = client_socket.recv(1024)
            user , message = pickle.loads(msg)

            if message == 'down()':
                users.remove(client_socket)
                for client in users:
                    client.send(pickle.dumps((user,"Left")))
                
                users.remove(user)
                
            


            for client in users:
                client.send(pickle.dumps((user,message)))        
                   
        except:
            print("Brute force close")
            
                
def threads():
    s.listen()
    while True:
        try:
            client_socket, addr = s.accept()
            user = client_socket.recv(1024).decode('utf-8')

            
            users.append(client_socket)
                        
            thread = threading.Thread(target=client, args=(client_socket, addr, user))
            thread.start()
            client_socket.send("jibrish".encode('utf-8'))
        
        except:
            s.close()
            
print("\033[1;32m[STARTING] Server!\033[0m \033[;1m")
threads()
