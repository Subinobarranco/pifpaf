#
https://www.youtube.com/watch?v=dY1R92kXhVo
#TCP/IPv4
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)

# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))

##tcp
import socket, time, sys
import threading

TCP_IP = ''
TCP_PORT = 8888
BUFFER_SIZE = 1024
CLIENTS = {}
clientCount = 0

def listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP,TCP_PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print("new connection from:"+ str(addr))
        #print(len(CLIENTS))
        global clientCount
        clientCount = clientCount+1
        print (clientCount)
        # register client
        CLIENTS[conn.fileno()] = conn


def broadcast():
     for client in CLIENTS.values():
            client.send('this is a broadcats msg')

if __name__ == '__main__':
    listener()

    while clientCount > 0:
        broadcast()
        print(len(CLIENTS)) #print out the number of connected clients every 5s
        time.sleep(5) 
