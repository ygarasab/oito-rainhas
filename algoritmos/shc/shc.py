from tabuleiro import Tabuleiro
from .caixinha import *


def simulated_aneeling(temperatura_inicial):
    tabuleiro_atual = Tabuleiro()
    temperatura = temperatura_inicial

    while 1:

        temperatura = reduz_temperatura(temperatura)
        if not temperatura:
            return tabuleiro_atual
        tabuleiro_seguinte = Tabuleiro()
        variacao = tabuleiro_atual - tabuleiro_seguinte
        if variacao > 0:
            tabuleiro_atual = tabuleiro_seguinte
        elif tabuleiro_deve_mudar(temperatura, variacao):
            tabuleiro_atual = tabuleiro_seguinte
