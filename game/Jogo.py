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
        v = self.valores[self.valor] + " of " + self.naipes[self.naipe]
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
        self.vitorias = 0
        self.carta = None
        self.nome = nome


class Game:
    def __init__(self):
        nome1 = input("p1 name ")
        nome2 = input("p2 name ")
        self.baralho = Baralho()
        self.p1 = Player(nome1)
        self.p2 = Player(nome2)

    def vitorias(self, vencedor):
        w = "{} wins this round"
        w = w.format(vencedor)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cartas = self.baralho.cartas
        print("beginning War!")
        while len(cartas) >= 2:
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.baralho.rm_carta()
            p2c = self.baralho.rm_carta()
            p1n = self.p1.nome
            p2n = self.p2.nome
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.vitorias += 1
                self.vitorias(self.p1.nome)
            else:
                self.p2.vitorias += 1
                self.vitorias(self.p2.nome)

        vit = self.vencedor(self.p1,
                         self.p2)
        print("War is over.{} wins"
              .format(vit))

    def vencedor(self, p1, p2):
        if p1.vitorias > p2.vitorias:
            return p1.nome
        if p1.vitorias < p2.vitorias:
            return p2.nome
        return "It was a tie!"

game = Game()
game.play_game()
