#UDP server responds to broadcast packets
#you can have more than one instance of these running
import socket, Util

def textver(baralho, monte):
    if len (baralho)>=2 and len(monte)>=2:
        return("q para fechar, c comprar do baralho, v coletar do monte e b para bater: ")
    if len (baralho)>=2:
        return("q para fechar, c comprar do baralho e b para bater: ")
    if len(monte)>=2:
        return("q para fechar, v coletar do monte e b para bater: ")

def escolha(pc):
    for x in range(len(pc)):
        txt = '{}--> {}'
        print(txt.format(x, pc[x]))
    respos=input("escolha  entre 0-9 ")
    return pc.pop(int(respos))

def mesa():
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

    #2players para teste funcional e depois expandir para 4player
    #criar baralho
    baralhos=Util.Baralho()
    baralho=baralhos.cartas
    #mao do proprio player e outros
    p1c=[]
    p2c=[]
    #monte de descarte que deve ser repasado a todos de seu ultimo estado
    monte=[]
    #TCP for the game
    ser=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.bind(('', 54545))
    ser.settimeout(10)
    ser.listen(1)
    conn, addr=ser.accept()
    with conn:
        #prencher mao de players
        print('conectado com ' + addr[0] + ':' + str(addr[1]))
        #conn.sendall(b'conectou')
        while True:
            dado = conn.recv(2048)
            dado= b'pronto para partida'
            conn.sendall(dado)
            if not dado:
                break
        dado= b'pronto para partida'
        conn.sendall(dado)
        #conn.close()

    #seguir partida
    #monte ser atualizado em todos em todos os casos
    #ultima carta para vencer, receber todos as cartas e repasar a todos
    #comandos de acontecimentos: c9-bater c8-monte c7-comprar
    #envio de carta index numero segundo index naipe
