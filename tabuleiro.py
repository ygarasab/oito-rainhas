import random


class Tabuleiro:

    def __init__(self, n_rainhas=8):
        self.n_rainhas = n_rainhas
        self.rainhas = [0 for _ in range(n_rainhas)]
        self.valor = 0
        self.aleatoriza()

    def aleatoriza(self):
        for i in range(self.n_rainhas):
            self.rainhas[i] = random.randint(0, self.n_rainhas - 1)

        self.calcula_valor()

    def calcula_valor(self):
        ataques = 0

        for indice_rainha in range(0, self.n_rainhas):
            for indice_prox_rainha in range(indice_rainha + 1, self.n_rainhas):
                ataques += self.ha_ataque(indice_rainha, indice_prox_rainha)  # ataque diagonal embaixo

        self.valor = ataques

    def ha_ataque(self, indice_a, indice_b):
        return (self.rainhas[indice_a] == self.rainhas[indice_b]  # ataque horizontal
                or (indice_b - indice_a) == abs(self.rainhas[indice_b] - self.rainhas[indice_a])) # ataque diagonal

    def __sub__(self, other):
        return self.valor - other.valor

    def __repr__(self):
        return str(self.rainhas)
