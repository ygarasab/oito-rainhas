import numpy as np
import typing as t

from . import erros


# noinspection SpellCheckingInspection,SpellCheckingInspection
class Tabuleiro:
    def __init__(self, n_rainhas=8, lado_tabuleiro=8):
        self.__lado_tabuleiro, self.__n_rainhas, self.__rainhas, self.__valor = None, None, None, np.inf

        self.lado_tabuleiro = lado_tabuleiro
        self.n_rainhas = n_rainhas

    @property
    def lado_tabuleiro(self):
        return self.__lado_tabuleiro

    @lado_tabuleiro.setter
    def lado_tabuleiro(self, novo_lado_tabuleiro):
        erros.verifica_tipo(lado_tabuleiro=(novo_lado_tabuleiro, "atributo", t.SupportsInt))

        novo_lado_tabuleiro = int(novo_lado_tabuleiro)

        erros.verifica_nao_negatividade(lado_tabuleiro=(novo_lado_tabuleiro, "atributo"))

        if self.n_rainhas is not None and novo_lado_tabuleiro < self.n_rainhas:
            raise ValueError("O atributo lado_tabuleiro precisa receber um número, no mínimo, igual ao atributo "
                             "n_rainhas.")

        self.__lado_tabuleiro = novo_lado_tabuleiro

    @property
    def n_rainhas(self):
        return self.__n_rainhas

    @n_rainhas.setter
    def n_rainhas(self, novo_n_rainhas):
        erros.verifica_tipo(n_rainhas=(novo_n_rainhas, "atributo", t.SupportsInt))

        novo_n_rainhas = int(novo_n_rainhas)

        erros.verifica_nao_negatividade(n_rainhas=(novo_n_rainhas, "atributo"))

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
        erros.verifica_tipo(valor=(novo_valor, "atributo", t.SupportsInt))

        novo_valor = int(novo_valor)

        erros.verifica_nao_negatividade(valor=(novo_valor, "atributo"))

        self.__valor = novo_valor

    def ha_ataque(self, indice_a, indice_b):
        erros.verifica_tipo(indice_a=(indice_a, "parâmetro", t.SupportsInt),
                            indice_b=(indice_b, "parâmetro", t.SupportsInt))

        indice_a, indice_b = int(indice_a), int(indice_b)

        ha_ataque_horizontal = self.rainhas[indice_a] == self.rainhas[indice_b]
        ha_ataque_diagonal = (indice_b - indice_a) == abs(self.rainhas[indice_b] - self.rainhas[indice_a])

        return ha_ataque_horizontal or ha_ataque_diagonal

    def __sub__(self, other):
        if not isinstance(other, Tabuleiro):
            raise TypeError("O operador '-' funciona apenas entre objetos Tabuleiro.")

        return self.valor - other.valor

    def __repr__(self):
        return f"[Tabuleiro] {self.rainhas} | {self.valor} ataques"
