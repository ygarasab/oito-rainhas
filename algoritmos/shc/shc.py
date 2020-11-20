from tabuleiro import Tabuleiro
from .caixinha import *


def simulated_annealing(temperatura_inicial):
    tabuleiro_atual = Tabuleiro()
    temperatura = temperatura_inicial

    print(f"Tabuleiro inicial: {tabuleiro_atual}  Ataques: {tabuleiro_atual.valor}")

    while 1:
        temperatura = reduz_temperatura(temperatura)

        if temperatura < 0:
            print(f"Tabuleiro final: {tabuleiro_atual}  Ataques: {tabuleiro_atual.valor}")
            break

        tabuleiro_seguinte = Tabuleiro()

        variacao = tabuleiro_atual - tabuleiro_seguinte
        
        if variacao > 0:
            tabuleiro_atual = tabuleiro_seguinte
        elif tabuleiro_deve_mudar(temperatura, variacao):
            tabuleiro_atual = tabuleiro_seguinte