import Util

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

#criar mao
def maoinicial(baralho,baralhos,p1c,p2c):
    for x in range(9):
        if len(baralho) >= 2:
            p1c.append(baralhos.rm_carta())
            p2c.append(baralhos.rm_carta())


def main():
    nome1 = input("p1 name ")
    nome2 = input("p2 name ")
    baralhos = Util.Baralho()
    baralho= baralhos.cartas
    p1 = Util.Player(nome1)
    p2 = Util.Player(nome2)
    z=0
    p1c=[]
    p2c=[]
    monte=[]

    maoinicial(baralho,baralhos,p1c,p2c)

    #comeca jogo
    print("beginning War!")
    while True:
        #z=z+1
        m=textver(baralho, monte)
        response = input(m)

        #fechar
        if response == 'q':
            break
        
        #comprar do baralho e descartar
        elif response == 'c':
            p1c.append(baralhos.rm_carta())
            p2c.append(baralhos.rm_carta())
            z=z+1
            monte.append(escolha(p1c))
            monte.append(escolha(p2c))
        
        #pegar do monte e descartar
        elif response == 'v':
            p1c.append(monte.pop())
            p2c.append(monte.pop())
            monte.append(escolha(p1c))
            monte.append(escolha(p2c))
            
        #bater
        elif response == 'b':
            print('\n')
            print(p1c)
            print('\n')
            print(p2c)
            break

        
        p1n = p1.nome
        p2n = p2.nome
        #self.draw(p1n, p1c, p2n, p2c)
        if p1c > p2c:
            print('vitoria p1')
        else:
            print('vitorias p2')

                        
    print("War is over.{} wins voltas " + format(z))
    print(p1c[1])
    print('\n')
    v, n=Util.decodi(p1c[1])
    print(v)
    print(n)
    print('\n')
    print(p1c[1])
    print(p1c[1].valor)
    print(p1c[1].naipe)
    print(Util.Carta((p1c[1].valor),(p1c[1].naipe)))
    print(Util.codifi(v,n))
    
main()
