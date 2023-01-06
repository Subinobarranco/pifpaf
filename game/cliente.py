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

def game(addr):
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect((addr,54545))
    teste=b"conectados?"
    cli.sendall(teste)
    cli.shutdown(socket.SHUT_WR)
    mao=[]
    monte=[]
    while True:
        #recebe o que pode fazer
        m=textver(baralho,monte)
        response=input(m)
        #envia resposta
        
        dado=cli.recv(2048)
        cli.send(b'cliente')
        if not dado:
            break
        print(dado)
        #cli.close()
            
    
    
    
    
