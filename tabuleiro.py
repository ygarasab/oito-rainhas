import numpy as np
import typing as t


# noinspection SpellCheckingInspection,SpellCheckingInspection
class Tabuleiro:
    def __init__(self, n_rainhas=8, lado_tabuleiro=8):
        self.__lado_tabuleiro = None
        self.__n_rainhas = None
        self.__rainhas = None
        self.__valor = np.inf

        self.lado_tabuleiro = lado_tabuleiro
        self.n_rainhas = n_rainhas

    @property
    def lado_tabuleiro(self):
        return self.__lado_tabuleiro

    @lado_tabuleiro.setter
    def lado_tabuleiro(self, novo_lado_tabuleiro):
        if not isinstance(novo_lado_tabuleiro, t.SupportsInt):
            raise TypeError("O atributo lado_tabuleiro precisa receber um número inteiro ou um objeto que possa ser "
                            "convertido para tal.")
        else:
            novo_lado_tabuleiro = int(novo_lado_tabuleiro)

        if novo_lado_tabuleiro < 0:
            raise ValueError("O atributo lado_tabuleiro precisa receber um número positivo.")
        if self.n_rainhas is not None and novo_lado_tabuleiro < self.n_rainhas:
            raise ValueError("O atributo lado_tabuleiro precisa receber um número, no mínimo, igual ao atributo "
                             "n_rainhas.")

        self.__lado_tabuleiro = novo_lado_tabuleiro

    @property
    def n_rainhas(self):
        return self.__n_rainhas

    @n_rainhas.setter
    def n_rainhas(self, novo_n_rainhas):
        if not isinstance(novo_n_rainhas, t.SupportsInt):
            raise TypeError("O atributo n_rainhas precisa receber um número inteiro ou um objeto que possa ser "
                            "convertido para tal.")
        else:
            novo_n_rainhas = int(novo_n_rainhas)

        if novo_n_rainhas < 0:
            raise ValueError("O atributo n_rainhas precisa receber um número positivo.")
        if self.lado_tabuleiro is not None and novo_n_rainhas > self.lado_tabuleiro:
            raise ValueError("O atributo n_rainhas não pode ser maior do que o atributo lado_tabuleiro.")

        self.__n_rainhas = novo_n_rainhas

        self.aleatoriza_rainhas()

    @property
    def rainhas(self):
        return self.__rainhas

    @rainhas.setter
    def rainhas(self, novo_rainhas):
        if not isinstance(novo_rainhas, np.ndarray):
            if isinstance(novo_rainhas, (list, tuple)):
                novo_rainhas = np.array(novo_rainhas, dtype=np.int_)
            else:
                raise TypeError("O atributo novo_rainhas precisa receber um array numpy.")

        if novo_rainhas.ndim > 1:
            raise ValueError("O atributo ndim do atributo rainhas precisa ser igual a 1.")

        if novo_rainhas.shape[0] < self.lado_tabuleiro:
            diferenca = self.lado_tabuleiro - novo_rainhas.shape[0]

            novo_rainhas = np.append(novo_rainhas, diferenca * [-1])
        elif novo_rainhas.shape[0] > self.lado_tabuleiro:
            raise TypeError("O comprimento de novo_rainhas precisa ser, no máximo, igual ao atributo lado_tabuleiro.")

        self.__rainhas = novo_rainhas

        self.calcula_valor()

    def aleatoriza_rainhas(self):
        rainhas = np.empty(self.lado_tabuleiro, dtype=np.int_)

        rainhas[:self.n_rainhas] = np.random.choice(self.lado_tabuleiro, self.n_rainhas, replace=False)
        rainhas[self.n_rainhas:] = -1

        self.rainhas = rainhas

    def calcula_valor(self):
        ataques = 0

        for indice_rainha in range(self.n_rainhas):
            for indice_prox_rainha in range(indice_rainha + 1, self.n_rainhas):
                ataques += self.ha_ataque(indice_rainha, indice_prox_rainha)  # ataque diagonal embaixo

        self.valor = ataques

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        if not isinstance(novo_valor, t.SupportsInt):
            raise TypeError("O atributo valor precisa receber um número inteiro ou um objeto que possa ser convertido "
                            "para tal.")
        else:
            novo_valor = int(novo_valor)

        # TODO: se pertinente, colocar verificações para que o valor (número de ataques) não exceda o lado do tabuleiro.

        self.__valor = novo_valor

    def ha_ataque(self, indice_a, indice_b):
        if not isinstance(indice_a, t.SupportsInt):
            raise TypeError("O parâmetro indice_a precisa receber um número inteiro ou um objeto que possa ser "
                            "convetido para tal.")
        else:
            indice_a = int(indice_a)

        if not isinstance(indice_b, t.SupportsInt):
            raise TypeError("O parâmetro indice_b precisa receber um número inteiro ou um objeto que possa ser "
                            "convertido para tal.")
        else:
            indice_b = int(indice_b)

        ha_ataque_horizontal = self.rainhas[indice_a] == self.rainhas[indice_b]
        ha_ataque_diagonal = (indice_b - indice_a) == abs(self.rainhas[indice_b] - self.rainhas[indice_a])

        return ha_ataque_horizontal or ha_ataque_diagonal

    def __sub__(self, other):
        if not isinstance(other, Tabuleiro):
            raise TypeError("O operador '-' funciona apenas entre objetos Tabuleiro.")

        return self.valor - other.valor

    def __repr__(self):
        return f"[Tabuleiro] {self.rainhas} | {self.valor} ataques"
