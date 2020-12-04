import numpy as np
import typing as t

from . import caixinha
from .. import checagens


# noinspection SpellCheckingInspection,SpellCheckingInspection
class Tabuleiro:
    def __init__(self, *, binario=False, lado_tabuleiro=8, n_rainhas=8, rainhas=None):
        self.__lado_tabuleiro, self.__n_rainhas, self.__rainhas, self.__valor = None, None, None, np.inf

        self.binario = binario
        self.lado_tabuleiro = lado_tabuleiro
        self.n_rainhas = n_rainhas

        if rainhas is not None:
            self.rainhas = rainhas

    @property
    def binario(self):
        return self.__binario

    @binario.setter
    def binario(self, novo_binario):
        novo_binario = checagens.verifica_tipo(binario=(novo_binario, "atributo", (bool, np.bool_)))

        self.__binario = novo_binario

        if self.__rainhas is not None:
            if novo_binario is True:
                numero_de_casas = np.ceil(np.log2(self.lado_tabuleiro + 1)).astype(np.int_)
                self.rainhas = [caixinha.decimal_para_binario(posicao, numero_de_casas) for posicao in self.rainhas]
            else:
                self.rainhas = [caixinha.binario_para_decimal(posicao) for posicao in self.rainhas]

    @property
    def lado_tabuleiro(self):
        return self.__lado_tabuleiro

    @lado_tabuleiro.setter
    def lado_tabuleiro(self, novo_lado_tabuleiro):
        novo_lado_tabuleiro = checagens.verifica_tipo(lado_tabuleiro=(novo_lado_tabuleiro, "atributo", t.SupportsInt))

        checagens.verifica_nao_negatividade(lado_tabuleiro=(novo_lado_tabuleiro, "atributo"))
        checagens.verifica_maior_ou_igual_a(lado_tabuleiro=(novo_lado_tabuleiro, "atributo"),
                                            n_rainhas=(self.n_rainhas, "atributo"))

        self.__lado_tabuleiro = novo_lado_tabuleiro

    @property
    def n_rainhas(self):
        return self.__n_rainhas

    @n_rainhas.setter
    def n_rainhas(self, novo_n_rainhas):
        novo_n_rainhas = checagens.verifica_tipo(n_rainhas=(novo_n_rainhas, "atributo", t.SupportsInt))

        checagens.verifica_nao_negatividade(n_rainhas=(novo_n_rainhas, "atributo"))
        checagens.verifica_menor_ou_igual_a(n_rainhas=(novo_n_rainhas, "atributo"),
                                            lado_tabuleiro=(self.lado_tabuleiro, "atributo"))

        self.__n_rainhas = novo_n_rainhas

        self.aleatoriza_rainhas()

    def aleatoriza_rainhas(self):
        posicoes = np.random.choice(self.lado_tabuleiro, self.n_rainhas, replace=False)

        if self.binario is True:
            digitos_necessarios = np.ceil(np.log2(self.lado_tabuleiro + 1)).astype(np.int_)
            rainhas = np.empty((self.lado_tabuleiro, digitos_necessarios), dtype=np.bool_)
            rainhas[:self.n_rainhas, :] = [caixinha.decimal_para_binario(posicao,
                                                                         digitos_necessarios) for posicao in posicoes]
            rainhas[self.n_rainhas:, :] = np.False_
        else:
            rainhas = np.empty(self.lado_tabuleiro, dtype=np.int_)

            rainhas[:self.n_rainhas] = posicoes
            rainhas[self.n_rainhas:] = -1

        self.rainhas = rainhas

    @property
    def rainhas(self):
        return self.__rainhas.copy() if self.__rainhas is not None else None

    @rainhas.setter
    def rainhas(self, novo_rainhas):
        novo_rainhas = checagens.verifica_tipo(rainhas=(novo_rainhas, "atributo", np.ndarray))

        checagens.verifica_comprimento_menor_ou_igual_a(rainhas=(novo_rainhas, "atributo"),
                                                        lado_tabuleiro=(self.lado_tabuleiro, "atributo"))

        if self.binario is True:
            novo_rainhas = checagens.verifica_dtype(rainhas=(novo_rainhas, "atributo", np.bool_))

            checagens.verifica_ndim(rainhas=(novo_rainhas, "atributo", 2))

            # novo_rainhas_decimal = np.array([caixinha.binario_para_decimal(posicao) for posicao in novo_rainhas])
            # checagens.verifica_rainhas_unicas(rainhas=(novo_rainhas_decimal, "atributo"))

            if novo_rainhas.shape[0] < self.lado_tabuleiro:
                diferenca = self.lado_tabuleiro - novo_rainhas.shape[0]
                novo_rainhas = np.concatenate((novo_rainhas, diferenca * [[np.False_, np.False_, np.False_]]))
        else:
            novo_rainhas = checagens.verifica_dtype(rainhas=(novo_rainhas, "atributo", np.int_))

            checagens.verifica_ndim(rainhas=(novo_rainhas, "atributo", 1))
            # checagens.verifica_rainhas_unicas(rainhas=(novo_rainhas, "atributo"))

            if novo_rainhas.shape[0] < self.lado_tabuleiro:
                diferenca = self.lado_tabuleiro - novo_rainhas.shape[0]
                novo_rainhas = np.append(novo_rainhas, diferenca * [-1])

        self.__rainhas = novo_rainhas

        self.calcula_valor()

    def calcula_valor(self):
        ataques = 0

        for indice_rainha in range(self.n_rainhas):
            for indice_prox_rainha in range(indice_rainha + 1, self.n_rainhas):
                ataques += self.ha_ataque(indice_rainha, indice_prox_rainha)  
                
        self.__valor = ataques

    @property
    def valor(self):
        return self.__valor

    def ha_ataque(self, indice_a, indice_b):
        if self.binario is True:
            iterador = (caixinha.binario_para_decimal(posicao) for posicao in self.rainhas)
            rainhas = np.fromiter(iterador, np.int_, self.n_rainhas)
        else:
            rainhas = self.rainhas

        indice_a = checagens.verifica_tipo(indice_a=(indice_a, "parâmetro", t.SupportsInt))
        indice_b = checagens.verifica_tipo(indice_b=(indice_b, "parâmetro", t.SupportsInt))

        ha_ataque_diagonal = (indice_b - indice_a) == abs(rainhas[indice_b] - rainhas[indice_a])

        return ha_ataque_diagonal

    @property
    def ha_rainhas_na_mesma_linha(self):
        if self.binario is True:
            iterador = (caixinha.binario_para_decimal(posicao) for posicao in self.rainhas)
            rainhas = np.fromiter(iterador, np.int_, self.n_rainhas)
        else:
            rainhas = self.rainhas

        rainhas = rainhas[rainhas != -1]

        return True if rainhas.shape[0] != np.unique(rainhas).shape[0] else False

    def __sub__(self, outro):
        checagens.verifica_tipo_operador('-', outro, Tabuleiro)

        return self.valor - outro.valor

    def __lt__(self, outro):
        checagens.verifica_tipo_operador('<', outro, Tabuleiro)

        return self.valor < outro.valor

    def __gt__(self, outro):
        checagens.verifica_tipo_operador('>', outro, Tabuleiro)

        return self.valor > outro.valor

    def __eq__(self, outro):
        checagens.verifica_tipo_operador('==', outro, Tabuleiro)

        return self.valor == outro.valor

    def __repr__(self):
        if self.binario is False:
            representacao_rainhas = str(self.rainhas)
            tipo = "Decimal"
        else:
            representacao_rainhas = caixinha.ajusta_indentacao(str(self.rainhas), 12 * ' ')
            tipo = "Binário"

        return f"[Tabuleiro] {representacao_rainhas} | {self.valor} ataques | {tipo}"

    def __str__(self):
        if self.binario is False:
            return str(self.rainhas.tolist())
        else:
            representacao = []

            for rainha in self.rainhas:
                string = ""

                for bit in rainha:
                    if bit is np.True_:
                        string += "1"
                    else:
                        string += "0"

                representacao.append(string)

            return str(representacao).replace("'", "")

    def __len__(self):
        return self.n_rainhas
