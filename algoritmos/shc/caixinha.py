import random, math, decimal


def reduz_temperatura(temperatura):
    return temperatura - 0.01


def tabuleiro_deve_mudar(temperatura, variacao):
    exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(variacao) / decimal.Decimal(temperatura)))
    return random.uniform(0, 1) < exp
