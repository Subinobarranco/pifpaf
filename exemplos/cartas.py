import socket
import threading
import random


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criacao do socket TCP
sock.bind((TCP_IP, TCP_PORT))
sock.settimeout(10)
sock.listen(1)


#simbolos dos naipes ASCCI
Paus = "\u2663"
Espadas = "\u2665"
Ouro = "\u2666"
Copas = "\u2660"

ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = (Copas, Espadas, Ouro, Paus)

deck = [r+s for r in ranks for s in suits]
hand_size = 9
#hands = []

clients = dict()

def deal(clients, deck, hand_size):
    random.shuffle(deck)

    for player in clients:
        hand = []
        for i in range(0, hand_size):
            hand.append(deck.pop())
        clients[player] = hand
        #hands.append(hand)

    send_message(clients[player], player) #mostrar a mão aos jogadores

    #print(hands)
    print(clients.items())

def process_message(arrClients, conn):
    if (arrClients[0] == "LOGIN" and len(arrClients) == 2):
        print("Tipo: login => " + arrClients[1])
        if arrClients[1] not in clients.keys():
            clients[arrClients[1]] = conn
            print (len(clients))
            print("Novo cliente logado: " + arrClients[1])
            send_message("LOGIN_OK", conn)
            #conn.send("LOGIN_OK".encode("utf-8"))
        else:
            print("Nome de usuário já está sendo usado: " + arrClients[1])
            send_message("LOGIN_KO", conn)
    else:
        print("Tipos dos numeros desconhecidos ou invalidos")


def send_message(msg, conn):
    conn.send(msg.encode("utf-8"))
    print("Mensagem enviada: " + msg)


def client(conn, addr):
    print("Thread Cliente: " + str(addr))

    while 1:
        data = conn.recv(BUFFER_SIZE)

        if not data: break

        data = data.decode("utf-8")
        arrClients = data.split("#")


        process_message(arrClients, conn)

    #conn.close()


while 1:
    if (len(clients)>=2):
        print("-----------------")
        comecar = input("Deseja comecar a jogar? S/N")
        if comecar == "S":

            deal(clients, deck, hand_size)

    elif len(clients)==6:
        deal(clients, deck, hand_size)

    else:

        print("Esperando por clientes...")
        try:
            conn, addr = sock.accept() # aceita a ligacao
            print("Endereco de conexao: " + str(addr))

            t = threading.Thread(target=client, args=(conn, addr))
            t.start()
        except socket.timeout:
            continue
