import random
import numpy as np
import pandas as pd

from ..tabuleiro import Tabuleiro


# noinspection SpellCheckingInspection
def gera_contagem_populacao(populacao):
    ataques = [tabuleiro.valor for tabuleiro in populacao]

    colunas = np.unique(ataques)
    indices = ["Contagem"]

    contagem_de_valores = {ataque: 0 for ataque in colunas}

    for ataque in ataques:
        contagem_de_valores[ataque] += 1

    data_frame = pd.DataFrame(contagem_de_valores, columns=colunas, index=indices)
    data_frame.columns.names = ["Ataques"]

    return data_frame
