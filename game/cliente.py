#UDP client broadcasts to server(s)
import socket, subprocess


#args= "server.py"
#Procurar partida, caso nao achar iniciar servidor
print('Iniciar procura')

address = ('<broadcast>', 54545)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

data = b'Tem partida?'
client_socket.sendto(data, address)

try:
    client_socket.settimeout(5)
    while True:
        recv_data, addr = client_socket.recvfrom(2048)
        print(addr,recv_data)
        if not addr:
            break
except:
    #exec(open("server.py").read())
    #p=subprocess.Popen(args)
    addr='localhost'
    
#TCP for the game
print("saiu de loop")
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(addr)
teste=b"conectados?"
cli.sendall(teste)
#cli.shutdown(socket.SHUT_WR)
while True:
    if keyboard.is_pressed('t'):
        cli.close()
        break
    dado=cli.recv(2048)
    cli.send(b'cliente')
    if not dado:
        break
    print(dado)
#cli.close()

