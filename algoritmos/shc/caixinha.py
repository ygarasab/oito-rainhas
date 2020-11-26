import decimal
import numpy as np
import typing as t

from .. import checagens


# noinspection SpellCheckingInspection
def gera_temperaturas(temperatura_inicial, variacao):
    n_iteracoes = np.round(np.floor(temperatura_inicial / variacao))
    temperaturas = temperatura_inicial - variacao * np.arange(n_iteracoes)

    return temperaturas


# noinspection SpellCheckingInspection
def tabuleiro_deve_mudar(temperatura, variacao):
    temperatura = checagens.verifica_tipo(temperatura=(temperatura, "parâmetro", t.SupportsFloat))
    variacao = checagens.verifica_tipo(variacao=(variacao, "parâmetro", t.SupportsFloat))
    e = float(np.e)

    exp = decimal.Decimal(decimal.Decimal(e) ** (decimal.Decimal(variacao) / decimal.Decimal(temperatura)))

    return np.random.uniform() < exp
