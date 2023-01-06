#UDP server responds to broadcast packets
#you can have more than one instance of these running
import socket, Util

def textver(baralho, monte):
    if len (baralho)>=2 and len(monte)>=2:
        return("c comprar do baralho, v coletar do monte e b para bater: ")
    if len (baralho)>=2:
        return("c comprar do baralho e b para bater: ")
    if len(monte)>=2:
        return("v coletar do monte e b para bater: ")

def escolha(pc):
    for x in range(len(pc)):
        txt = '{}--> {}'
        print(txt.format(x, pc[x]))
    respos=input("escolha  entre 0-9 ")
    return pc.pop(int(respos))

def maoinicial(baralho,baralhos,p1c,p2c):
    for x in range(9):
        if len (baralho)>=2:
            p1c.append(baralhos.rm_carta())
            p2c.append(baralhos.rm_carta())

def atualizarmonte(cart):
    #envia carta para todos players
    pass

def atualizaremovermonte():
    pass

def attodos(adress,p1c):
    pass

def mesa(procura=1):
    address = ('', 54545)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.bind(address)
    msg=localip=socket.gethostbyname(socket.gethostname())

    while procura==1:
        print ("Listening")
        recv_data, addr = server_socket.recvfrom(2048)
        if recv_data == b"Tem partida?":
            print (addr,':',recv_data)
            server_socket.sendto(msg.encode(), addr)
            break

    #2players para teste funcional e depois expandir para 4player
    players=[]
    p1=Util.Player('Player1')
    p2=Util.Player('Player2')
    p3=Util.Player('Player3')
    p4=Util.Player('Player4')
    players.append(p1)
    players.append(p2)
    players.append(p3)
    players.append(p4)
    #criar baralho
    baralhos=Util.Baralho()
    baralho=baralhos.cartas
    #mao do proprio player e outros
    p1c=[]
    p2c=[]
    #monte de descarte que deve ser repasado a todos de seu ultimo estado
    monte=[]
    #vez de qual player
    vezplayer=0
    #TCP for the game
    ser=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.bind(('', 54545))
    ser.settimeout(30)
    ser.listen(1)
    conn, addr=ser.accept()
    with conn:
        #criar mao de players
        maoinicial(baralho,baralhos,p1c,p2c)
        players[0].cartas=p1c
        players[1].cartas=p2c
        #attodos(addr,players[1].cartas=p2c)
        print('conectado com ' + addr[0] + ':' + str(addr[1]))
        #conn.sendall(b'conectou')
        while True:
            #escolhas do que fazer e verificar quem joga
            m=textver(baralho,monte)
            if vezplayer==0:
                response=input(m)

                #comprar do baralho e descartar
                if response == 'c':
                    players[vezplayer].cartas.append(baralhos.rm_carta())
                    monte.append(escolha(players[vezplayer].cartas))
                    atualizarmonte()
                
                #pegar do monte e descartar
                elif response == 'v':
                    players[vezplayer].cartas.append(monte.pop())
                    monte.append(escolha(players[vezplayer].cartas))
                    atualizarmonte()
                    
                #bater
                elif response == 'b':
                    print('\n')
                    print(players[vezplayer].cartas)
                    break
            else:
                conn.sendall(m.encode())
                dado = conn.recv(2048)
                response=dado.decode()

                #comprar do baralho e descartar
                if response == 'c':
                    valorenviar,naipenviar=Util.decodi(baralhos.rm_carta())
                    conn.sendall(str(valorenviar).encode())
                    conn.sendall(str(naipenviar).encode())

                    valoreceber=int(conn.recv(2048).decode())
                    naipeber=int(conn.recv(2048).decode())
                    monte.append(Util.Carta(valoreceber,naipeber))
                    atualizarmonte()
                
                #pegar do monte e descartar
                elif response == 'v':
                    valorenviar,naipenviar=Util.decodi(monte.pop())
                    conn.sendall(str(valorenviar).encode())
                    conn.sendall(str(naipenviar).encode())

                    valoreceber=int(conn.recv(2048).decode())
                    naipeber=int(conn.recv(2048).decode())
                    monte.append(Util.Carta(valoreceber,naipeber))
                    #atualizaremovermonte()
                    
                #bater
                elif response == 'b':
                    print('\n')
                    print(p1c)
                    print('\n')
                    print(p2c)
                    break
            
            #fechar
            if response == 'q':
                break
            
            
            #coneçao
            dado = conn.recv(2048)
            dado= b'pronto para partida'
            conn.sendall(dado)
            if not dado:
                break
            
            if vezplayer==3:
                vezplayer=0
            else:
                vezplayer=vezplayer+1
                
        dado= b'pronto para partida'
        conn.sendall(dado)
        #conn.close()

    print('\nBatido ')

    #seguir partida
    #monte ser atualizado em todos em todos os casos
    #ultima carta para vencer, receber todos as cartas e repasar a todos
    #comandos de acontecimentos: c9-bater c8-monte c7-comprar
    #envio de carta index numero segundo index naipe
