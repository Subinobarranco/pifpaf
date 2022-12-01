#UDP server responds to broadcast packets
#you can have more than one instance of these running
import socket
address = ('', 54545)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(address)
msg=localip=socket.gethostbyname(socket.gethostname())

while True:
    print ("Listening")
    recv_data, addr = server_socket.recvfrom(2048)
    if recv_data == b"Tem partida?":
        print (addr,':',recv_data)
        server_socket.sendto(msg.encode(), addr)
        break

ser=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind(('', 54545))
ser.listen(20)
client_socket, addr=ser.accept()
print('conectado com ' + addr[0] + ':' + str(addr[1]))

