#TCP for the game
import socket, random

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
            
    #dois baralhos de 1a13dos4naipes, representado por valor e depois naipe
    nivel=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    naipe=(0, 1, 2, 3) #(Paus, Espadas, Ouro, Copas)
    tamao= 9
    baralho=[r+s for r in nivel for s in naipe]
    for x in baralho:
        print(x)
    #definir primeiro jogador(que tira carta do monte)
    #player define comprar ou pegar do monte(atualizar todos)
    if(input("1 para comprar da pilha ou 0 para")==1):
        None
    else:
        None
    #logo apos ultimo movimento descartar uma carta(atualizar todos)
    #ao vencer ao comprar a ultima carta ou pegando do descarte,informar ao servidor
    #servidor deve receber todas as cartas e repassar ao outros quem bateu e quais cartas
    # apos noticia mandar confirmacao
    #caso queira reiniciar partida apos termino
    
    
