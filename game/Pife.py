#UDP client broadcasts to server(s)
import socket, cliente, server

#Procurar partida, caso nao achar iniciar servidor
print('Iniciar procura')

address = ('<broadcast>', 54545)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

data = b'Tem partida?'
client_socket.settimeout(10)

client_socket.sendto(data, address)
print('Tentando conectar')

try:
    print('Tentando conectar')
    recv_data, addr = client_socket.recvfrom(2048)
except:
    addr=''
    
print("saiu de loop")

if addr=='':
    server.mesa()
else:
    cliente.game(addr)

