import random

class Tabuleiro:

    def __init__(self, n_rainhas=8):
        self.n_rainhas = n_rainhas
        self.rainhas = [0 for _ in range(n_rainhas)]
        self.valor = 0
        self.aleatoriza()

    def aleatoriza(self):        
        for i in range(self.n_rainhas):
            self.rainhas[i] = random.randint(0, self.n_rainhas-1)

        self.calcula_valor()

    def calcula_valor(self):
        ataques = 0

        for indice_rainha in range(0, self.n_rainhas):
            distancia_diagonal = 1 
            for indice_prox_rainha in range(indice_rainha + 1, self.n_rainhas):
                if (self.rainhas[indice_rainha] == self.rainhas[indice_prox_rainha] # ataque horizontal
                    or self.rainhas[indice_prox_rainha] == self.rainhas[indice_rainha] - distancia_diagonal # ataque diagonal em cima
                    or self.rainhas[indice_prox_rainha] == self.rainhas[indice_rainha] + distancia_diagonal): # ataque diagonal embaixo
                    ataques += 1
                
                distancia_diagonal += 1
        
        self.valor = ataques

    def __sub__(self, other):
        return self.valor - other.valor

    def __repr__(self):
        return str(self.rainhas)