#UDP client broadcasts to server(s)
import socket

address = ('<broadcast>', 54545)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

data = b'Tem partida?'
client_socket.sendto(data, address)
while True:
    recv_data, addr = client_socket.recvfrom(2048)
    print(addr,recv_data)
    if addr is not None:
        break

#TCP for the game
print("saiu de loop")
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(addr)
cli.sendall(b"conectados?")
#cli.shutdown(socket.SHUT_WR)
while True:
    dado=cli.recv(2048)
    if not dado:
        break
    print(dado)
#cli.close()

