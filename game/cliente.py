#TCP for the game
import socket

class cliente:
    def main(addr)

def main(addr):
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

