from cliente import game
from server import mesa
x=input("1 para cliente ou 0 para servidor")
if(x=='1'):
    game("localhost")
else:
    mesa('localhost')

#https://thecleverprogrammer.com/2020/10/04/card-game-with-python/
#https://pense-python.caravela.club/18-heranca/01-objetos-card.html
