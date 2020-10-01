import socket, sys, threading, getpass, os, pickle

os.system('clear')
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5558
SERVER = socket.gethostbyname(socket.gethostname())
serv = input("Enter the ip: ")
c.connect((serv, PORT))
user = getpass.getuser()

c.send(user.encode('utf-8'))

print("Welcome to the chat-server")
print("Type 'down()' to quit")
msg = ''
while True:
    message = c.recv(7).decode('utf-8')
    if message == "jibrish":
        break
    else:
        msg += message
        if len(message)==0:
            break
print(msg)

def send():
    while True:
        try:
            sys.stdout.write(f"\033[1;32m{user} (me): \033[0m \033[;1m"); sys.stdout.flush()
            message = input()

            if message == "down()":
                c.send(pickle.dumps((user, message)))
                print("Bye")
                c.close()
                sys.exit()

            c.send(pickle.dumps((user, message)))
        except:
            print("Error while Sending!")

def receive():
    while True:
        try:
            msg = c.recv(1024)
            USER, MESSAGE = pickle.loads(msg)

            print(f"\n{USER}: {MESSAGE}")
            sys.stdout.write(f"\033[1;32m{user} (me): \033[0m \033[;1m"); sys.stdout.flush()
        except:
            break


send_thread = threading.Thread(target=send)
receive_thread = threading.Thread(target=receive)


send_thread.start()
receive_thread.start()
