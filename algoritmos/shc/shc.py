from ..tabuleiro import Tabuleiro
from .caixinha import *


# noinspection SpellCheckingInspection
def simulated_annealing(temperatura_inicial, variacao, verboso=False):
    tabuleiro_atual = Tabuleiro()
    temperaturas = gera_temperaturas(temperatura_inicial, variacao)

    if verboso is True:
        print(f"[Iteração -1] {tabuleiro_atual}")

    for iteracao, temperatura in enumerate(temperaturas):
        tabuleiro_seguinte = Tabuleiro()

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
