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
        novo_lado_tabuleiro = erros.verifica_tipo(lado_tabuleiro=(novo_lado_tabuleiro, "atributo", t.SupportsInt))

        erros.verifica_nao_negatividade(lado_tabuleiro=(novo_lado_tabuleiro, "atributo"))
        erros.verifica_maior_ou_igual_a(lado_tabuleiro=(novo_lado_tabuleiro, "atributo"),
                                        n_rainhas=(self.n_rainhas, "atributo"))

        self.__lado_tabuleiro = novo_lado_tabuleiro

    @property
    def n_rainhas(self):
        return self.__n_rainhas

    @n_rainhas.setter
    def n_rainhas(self, novo_n_rainhas):
        novo_n_rainhas = erros.verifica_tipo(n_rainhas=(novo_n_rainhas, "atributo", t.SupportsInt))

        erros.verifica_nao_negatividade(n_rainhas=(novo_n_rainhas, "atributo"))
        erros.verifica_menor_ou_igual_a(n_rainhas=(novo_n_rainhas, "atributo"),
                                        lado_tabuleiro=(self.lado_tabuleiro, "atributo"))

        self.__n_rainhas = novo_n_rainhas

        self.aleatoriza_rainhas()

    @property
    def rainhas(self):
        return self.__rainhas

    @rainhas.setter
    def rainhas(self, novo_rainhas):
        novo_rainhas = erros.verifica_tipo(rainhas=(novo_rainhas, "atributo", np.ndarray)).astype(np.int_)

        erros.verifica_ndim(rainhas=(novo_rainhas, "atributo", 1))
        erros.verifica_comprimento_menor_ou_igual_a(rainhas=(novo_rainhas, "atributo"),
                                                    lado_tabuleiro=(self.lado_tabuleiro, "atributo"))

        if novo_rainhas.shape[0] < self.lado_tabuleiro:
            diferenca = self.lado_tabuleiro - novo_rainhas.shape[0]
            novo_rainhas = np.append(novo_rainhas, diferenca * [-1])

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
        novo_valor = erros.verifica_tipo(valor=(novo_valor, "atributo", t.SupportsInt))

        erros.verifica_nao_negatividade(valor=(novo_valor, "atributo"))

        self.__valor = novo_valor

    def ha_ataque(self, indice_a, indice_b):
        indice_a = erros.verifica_tipo(indice_a=(indice_a, "parâmetro", t.SupportsInt))
        indice_b = erros.verifica_tipo(indice_b=(indice_b, "parâmetro", t.SupportsInt))

        ha_ataque_horizontal = self.rainhas[indice_a] == self.rainhas[indice_b]
        ha_ataque_diagonal = (indice_b - indice_a) == abs(self.rainhas[indice_b] - self.rainhas[indice_a])

        return ha_ataque_horizontal or ha_ataque_diagonal

    def __sub__(self, outro):
        erros.verifica_tipo_operador('-', outro, Tabuleiro)

        return self.valor - outro.valor

    def __repr__(self):
        return f"[Tabuleiro] {self.rainhas} | {self.valor} ataques"
