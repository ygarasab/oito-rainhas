import decimal
import numpy as np


# noinspection SpellCheckingInspection
def reduz_temperatura(temperatura):
    return temperatura - 0.01


# noinspection SpellCheckingInspection
def tabuleiro_deve_mudar(temperatura, variacao):
    exp = decimal.Decimal(decimal.Decimal(np.e) ** (decimal.Decimal(variacao) / decimal.Decimal(temperatura)))

    return np.random.uniform() < exp
