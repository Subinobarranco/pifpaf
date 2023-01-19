import socket, Util
from time import sleep

def escolha(pc):
    for x in range(len(pc)):
        txt = '{}--> {}'
        print(txt.format(x, pc[x]))
    respos=input("escolha  entre 0-9 ")
    return pc.pop(int(respos))

def game(addr):
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(addr)
    #teste=b"conectados?"
    #cli.sendall(teste)
    #cli.shutdown(socket.SHUT_WR)
    cli.settimeout(90)
    mao=[]
    monte=[]
    while True:
        cli.settimeout(150)
        #recebe o que vai acontecer
        while True:
            dado=(cli.recv(2048).decode())
            if dado:
                break

        if dado=='terminado':
            print('batido por outro player')
            batid=[]
            cli.settimeout(19)
            while len(batid) <= 8:
                #while True:
                valoreceber=int(cli.recv(2048).decode())
                    #if valoreceber:
                        #break
                naipeber=int(cli.recv(2048).decode())
                batid.append(Util.Carta(valoreceber,naipeber))
            print(batid)
            break
        
        if dado=='cartas a enviar':
            cli.settimeout(19)
            while len(mao) <= 8:
                #while True:
                valoreceber=int(cli.recv(2048).decode())
                    #if valoreceber:
                        #break
                naipeber=int(cli.recv(2048).decode())
                mao.append(Util.Carta(valoreceber,naipeber))
                #print(mao)
            print(mao)

        if dado=='monte':
            valoreceber=int(cli.recv(2048).decode())
            naipeber=int(cli.recv(2048).decode())
            monte.append(Util.Carta(valoreceber,naipeber))
            #print(monte)

        if dado=='monteremover':
            monte.pop()
            valoreceber=int(cli.recv(2048).decode())
            naipeber=int(cli.recv(2048).decode())
            monte.append(Util.Carta(valoreceber,naipeber))
            #print(monte)
            
        if dado=='resposta':
            dado=(cli.recv(2048).decode())
            print('\n\n\n\n')
            if monte:
                print('monte->')
                print(monte[-1])
            m=dado
            response=input(m)
            #comprar do baralho e descartar
            if response == 'c':
                cli.sendall(b'c')
                valoreceber=int(cli.recv(2048).decode())
                naipeber=int(cli.recv(2048).decode())
                mao.append(Util.Carta(valoreceber,naipeber))
                pc=escolha(mao)

                valorenviar,naipenviar=Util.decodi(pc)
                cli.sendall(str(valorenviar).encode())
                cli.sendall(str(naipenviar).encode())
                
            #pegar do monte e descartar
            elif response == 'v':
                cli.sendall(b'v')
                mao.append(monte.pop())
                pc=escolha(mao)
                monte.append(pc)
                valorenviar,naipenviar=Util.decodi(pc)
                cli.sendall(str(valorenviar).encode())
                cli.sendall(str(naipenviar).encode())
                
                    
            #bater
            elif response == 'b':
                cli.sendall(b'b')
                print('\n')
                print(mao)
                while len(mao):
                    print('cartas restantes a enviar')
                    print(len(mao))
                    valorenviar,naipenviar=Util.decodi(mao.pop())
                    cli.sendall(str(valorenviar).encode())
                    sleep(1)
                    cli.sendall(str(naipenviar).encode())
                    #sleep(1)
                break
            
        
        #dado=cli.recv(2048)
        #cli.send(b'cliente')
        #if not dado:
            #break
        #print(dado)
        print('\n')
        #cli.close()
            
    
    
    
    
