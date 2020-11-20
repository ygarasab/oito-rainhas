from tabuleiro import Tabuleiro
from .caixinha import *


# noinspection SpellCheckingInspection
def simulated_annealing(temperatura_inicial, verboso=False):
    tabuleiro_atual = Tabuleiro()
    temperatura, iteracao = temperatura_inicial, 0

    if verboso is True:
        print(f"[Iteração 0] {tabuleiro_atual}")

    while True:
        iteracao += 1

        temperatura = reduz_temperatura(temperatura)

        if temperatura < 0:
            if verboso is True:
                print("A temperatura chegou a zero.")

            return tabuleiro_atual

        tabuleiro_seguinte = Tabuleiro()

        variacao = tabuleiro_atual - tabuleiro_seguinte
        
        if variacao > 0:
            tabuleiro_atual = tabuleiro_seguinte
        elif tabuleiro_deve_mudar(temperatura, variacao):
            tabuleiro_atual = tabuleiro_seguinte

        if verboso is True:
            print(f"[Iteração {iteracao}] {tabuleiro_atual} [Temperatura {temperatura}]")
