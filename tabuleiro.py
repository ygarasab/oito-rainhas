class Tabuleiro:

    def __init__(self, n_rainhas=8):
        self.n_rainhas = n_rainhas
        self.rainhas = [0 for _ in range(n_rainhas)]
        self.valor = 0
        self.aleatoriza()

    def aleatoriza(self):
        # muda self.rainhas pra um ponto aleatorio
        self.calcula_valor()

    def calcula_valor(self):
        # calcula valor baseado na função objetivo
        pass

    def __sub__(self, other):
        return self.valor - other.valor
