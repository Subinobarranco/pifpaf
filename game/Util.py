from random import shuffle


class Carta:
    naipes = ["Paus", "Espadas", "Ouros", "Copas"]

    valores = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

    def __init__(self, v, n):
        """naipe + valor are ints"""
        self.valor = v
        self.naipe = n

    def __lt__(self, c2):
        if self.valor < c2.valor:
            return True
        if self.valor == c2.valor:
            if self.naipe < c2.naipe:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.valor > c2.valor:
            return True
        if self.valor == c2.valor:
            if self.naipe > c2.naipe:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.valores[self.valor] + " de " + self.naipes[self.naipe]
        return v


class Baralho:

    def __init__(self):
        self.cartas = []
        for x in range(2):
            for i in range(13):
                for j in range(4):
                    self.cartas.append(Carta(i, j))
        shuffle(self.cartas)

    def rm_carta(self):
        if len(self.cartas) == 0:
            return
        return self.cartas.pop()

class Player:
    def __init__(self, nome):
        self.carta = []
        self.nome = nome
