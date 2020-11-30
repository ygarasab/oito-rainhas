from ..tabuleiro import Tabuleiro
from .caixinha import *


# noinspection SpellCheckingInspection
def simulated_annealing(temperatura_inicial=100, variacao=.01, verboso=False):
    tabuleiro_atual = Tabuleiro(binario=True)
    temperaturas = gera_temperaturas(temperatura_inicial, variacao)

    if verboso is True:
        print(f"[Iteração -1] {tabuleiro_atual}")

    if tabuleiro_atual.valor == 0:
        return tabuleiro_atual, 0

    for iteracao, temperatura in enumerate(temperaturas):
        tabuleiro_seguinte = Tabuleiro(binario=True)

        if tabuleiro_seguinte.valor == 0:
            return tabuleiro_seguinte, iteracao + 1

        variacao = tabuleiro_atual - tabuleiro_seguinte
        
        if variacao > 0:
            tabuleiro_atual = tabuleiro_seguinte
        elif tabuleiro_deve_mudar(temperatura, variacao):
            tabuleiro_atual = tabuleiro_seguinte

        if verboso is True:
            print(f"[Iteração {iteracao}] {tabuleiro_atual} [Temperatura {np.round(temperatura, 3)}]")

    if verboso is True:
        print("A temperatura chegou a zero.")

    return tabuleiro_atual
