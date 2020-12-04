import decimal as d
import numpy as np
import typing as t

from .. import checagens


# noinspection SpellCheckingInspection
def gera_temperaturas(temperatura_inicial, variacao):
    temperatura_inicial = checagens.verifica_tipo(temperatura_inicial=(temperatura_inicial, "parâmetro",
                                                                       t.SupportsFloat))
    variacao = checagens.verifica_tipo(variacao=(variacao, "parâmetro", t.SupportsFloat))

    n_iteracoes = np.round(np.floor(temperatura_inicial / variacao))
    temperaturas = temperatura_inicial - variacao * np.arange(n_iteracoes)

    return temperaturas


# noinspection SpellCheckingInspection
def tabuleiro_deve_mudar(temperatura, variacao):
    temperatura = checagens.verifica_tipo(temperatura=(temperatura, "parâmetro", t.SupportsFloat))
    variacao = checagens.verifica_tipo(variacao=(variacao, "parâmetro", t.SupportsFloat))
    e = float(np.e)

    exp = d.Decimal(d.Decimal(e) ** (d.Decimal(variacao) / d.Decimal(temperatura)))

    return np.random.uniform() < exp
