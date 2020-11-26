import numpy as np
import random

from ..tabuleiro import Tabuleiro


# noinspection SpellCheckingInspection
def inicializa_populacao(tamanho_populacao):
    populacao = [Tabuleiro() for _ in range(tamanho_populacao)]

    return sorted(populacao)


# noinspection SpellCheckingInspection
def gera_nova_populacao(populacao, tamanho, taxa_crossover, taxa_mutacao):
    nova_populacao = []

    while len(nova_populacao) < tamanho:
        pais = selecao_dos_pais(populacao)
        filhos = cruzamento(pais, taxa_crossover)
        filhos = mutacao(filhos, taxa_mutacao)
        nova_populacao.extend(filhos)

    return sorted(nova_populacao)


# 3-Way Tournament Selection: selecionamos 3 indivíduos aleatórios da população para "lutar" entre si e ganha o que
# tiver melhor fitness.
# noinspection SpellCheckingInspection
def selecao_dos_pais(populacao):
    pais = []

    for _ in range(2):
        lutadores = random.sample(populacao, 3)
        lutadores = sorted(lutadores)

        if lutadores[0] in pais:
            pais.append(lutadores[1])
        else:
            pais.append(lutadores[0])

    return pais


# Cruzamento com ponto de corte aleatório
# noinspection SpellCheckingInspection
def cruzamento(pais, taxa_crossover):
    pai1 = pais[0]
    pai2 = pais[1]

    n = len(pai1)
    c = random.randint(0, n - 1)

    if np.random.uniform() <= taxa_crossover:
        filho1 = Tabuleiro()
        filho1.rainhas = np.append(pai1.rainhas[0:c], pai2.rainhas[c:n])

        filho2 = Tabuleiro()
        filho2.rainhas = np.append(pai2.rainhas[0:c], pai1.rainhas[c:n])

        filhos = [filho1, filho2]

    else:
        filhos = [pai1, pai2]

    return filhos


# Mutação com permutação com posição aleatória
# noinspection SpellCheckingInspection
def mutacao(filhos, taxa_mutacao):
    if np.random.uniform() <= taxa_mutacao:
        tam = len(filhos[0])

        for filho in filhos:
            index1 = random.randint(0, tam - 1)
            index2 = random.randint(0, tam - 1)

            filho.rainhas[index1], filho.rainhas[index2] = filho.rainhas[index2], filho.rainhas[index1]

    return filhos


# Retorna os melhores indivíduos da população antiga e da nova
# noinspection SpellCheckingInspection
def seleciona_sobreviventes(populacao, nova_populacao):
    sobreviventes = sorted(populacao + nova_populacao)

    return sobreviventes[:len(populacao)]
