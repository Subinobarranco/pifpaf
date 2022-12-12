#UDP client broadcasts to server(s)
import socket, cliente, server

#Procurar partida, caso nao achar iniciar servidor
print('Iniciar procura')

address = ('<broadcast>', 54545)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

data = b'Tem partida?'
client_socket.settimeout(2)

for x in range(3):
    client_socket.sendto(data, address)
    print('Tentando conectar')
    try:
        while True:
            recv_data, addr = client_socket.recvfrom(2048)
            print(addr,recv_data)
            if not addr:
                break
    except:
        addr=('localhost', 54545)
        pass


#TCP for the game
print("saiu de loop")

if addr=='localhost':
    ser = server.main(addr)
else
    cli = cliente.main(addr)

#https://pense-python.caravela.club/18-heranca/01-objetos-card.html
