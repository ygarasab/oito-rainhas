import numpy as np
import typing as t

from . import caixinha
from .. import checagens
from ..tabuleiro import Tabuleiro


# noinspection SpellCheckingInspection
def recozimento_simulado(temperatura_inicial=100, variacao=.01, binario=False, verboso=False):
    temperatura_inicial = checagens.verifica_tipo(temperatura_inicial=(temperatura_inicial, "parâmetro",
                                                                       t.SupportsFloat))
    variacao = checagens.verifica_tipo(variacao=(variacao, "parâmetro", t.SupportsFloat))
    verboso = checagens.verifica_tipo(verboso=(verboso, "parâmetro", (bool, np.bool_)))

    checagens.verifica_menor_ou_igual_a(variacao=(variacao, "parâmetro"),
                                        temperatura_inicial=(temperatura_inicial, "parâmetro"))

    tabuleiro_atual = Tabuleiro(binario=binario)
    temperaturas = caixinha.gera_temperaturas(temperatura_inicial, variacao)

    if verboso is True:
        print(f"[Iteração -1] {tabuleiro_atual}")

    if tabuleiro_atual.valor == 0:
        return tabuleiro_atual, 0

    for iteracao, temperatura in enumerate(temperaturas):
        tabuleiro_seguinte = Tabuleiro(binario=binario)

        if tabuleiro_seguinte.valor == 0:
            return tabuleiro_seguinte, iteracao + 1

        variacao = tabuleiro_atual - tabuleiro_seguinte
        
        if variacao > 0:
            tabuleiro_atual = tabuleiro_seguinte
        elif caixinha.tabuleiro_deve_mudar(temperatura, variacao):
            tabuleiro_atual = tabuleiro_seguinte

        if verboso is True:
            print(f"[Iteração {iteracao}] {tabuleiro_atual} [Temperatura {np.round(temperatura, 3)}]")

    if verboso is True:
        print("A temperatura chegou a zero.")

    return tabuleiro_atual
