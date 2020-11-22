import decimal
import numpy as np


# noinspection SpellCheckingInspection
def gera_temperaturas(temperatura_inicial, variacao):
    n_iteracoes = np.round(np.floor(temperatura_inicial / variacao))
    temperaturas = temperatura_inicial - variacao * np.arange(n_iteracoes)

    return temperaturas


# noinspection SpellCheckingInspection
def tabuleiro_deve_mudar(temperatura, variacao):
    exp = decimal.Decimal(decimal.Decimal(np.e) ** (decimal.Decimal(variacao) / decimal.Decimal(temperatura)))

    return np.random.uniform() < exp
