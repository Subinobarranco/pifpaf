#TCP for the game
import socket, Util

def game(addr):
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(addr)
    teste=b"conectados?"
    cli.sendall(teste)
    cli.shutdown(socket.SHUT_WR)
    while True:
        dado=cli.recv(2048)
        cli.send(b'cliente')
        if not dado:
            break
        print(dado)
        #cli.close()
            
    
    
    
    
