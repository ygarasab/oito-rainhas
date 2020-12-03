import numpy as np
import random as r

from ..tabuleiro import Tabuleiro


# noinspection SpellCheckingInspection
def inicializa_populacao(tamanho_populacao):
    populacao = [Tabuleiro(binario=True) for _ in range(tamanho_populacao)]

    return sorted(populacao)


# noinspection SpellCheckingInspection
def gera_nova_populacao(populacao, taxa_crossover, taxa_mutacao, tamanho_ringue):
    nova_populacao, tamanho_populacao = [], len(populacao)

    while len(nova_populacao) < tamanho_populacao:
        pais = selecao_dos_pais(populacao, tamanho_ringue)
        filhos = cruzamento(pais, taxa_crossover)
        filhos = mutacao(filhos, taxa_mutacao)
        nova_populacao.extend(filhos)

    return sorted(nova_populacao)


# noinspection SpellCheckingInspection
def nova_gera_nova_populacao(populacao, taxa_crossover, taxa_mutacao, tamanho_ringue):
    pais = nova_selecao_dos_pais(populacao, tamanho_ringue)
    filhos = gera_filhos_validos(pais, taxa_crossover, taxa_mutacao)

    return sorted(filhos)


# noinspection SpellCheckingInspection
def gera_filhos_validos(pais, taxa_crossover, taxa_mutacao):
    filhos, tamanho_populacao = [], len(pais)

    while len(filhos) < tamanho_populacao:
        embrioes = novo_cruzamento(pais, taxa_crossover)
        fetos = nova_mutacao(embrioes, taxa_mutacao)

        for feto in fetos:
            if len(filhos) < tamanho_populacao:
                if feto.ha_rainhas_na_mesma_linha is False:
                    filhos.append(feto)
            else:
                break

    return filhos


# 3-Way Tournament Selection: selecionamos 3 indivíduos aleatórios da população para "lutar" entre si e ganha o que
# tiver melhor fitness.
# noinspection SpellCheckingInspection
def selecao_dos_pais(populacao, tamanho_ringue):
    pais = []

    for _ in range(2):
        lutadores = r.sample(populacao, tamanho_ringue)
        lutadores = sorted(lutadores)

        if lutadores[0] in pais:
            pais.append(lutadores[1])
        else:
            pais.append(lutadores[0])

    return pais


# noinspection SpellCheckingInspection
def nova_selecao_dos_pais(populacao, tamanho_ringue):
    nova_populacao, tamanho_populacao = [], len(populacao)

    for _ in range(tamanho_populacao):
        lutadores = r.sample(populacao, tamanho_ringue)
        lutadores = sorted(lutadores)

        nova_populacao.append(lutadores[0])

    return nova_populacao


# noinspection SpellCheckingInspection
def selecao_dos_pais2(populacao, tamanho_ringue=3):
    nova_populacao = []

    for _ in range(2):
        lutadores = r.sample(populacao, tamanho_ringue)
        lutadores = sorted(lutadores)

        if np.random.random() <= .5:
            nova_populacao.append(lutadores[0])
        else:
            nova_populacao.append(lutadores[-1])

    return nova_populacao


# Cruzamento com ponto de corte aleatório
# noinspection SpellCheckingInspection
def cruzamento(pais, taxa_crossover):
    pai1, pai2 = pais[0], pais[1]

    if np.random.uniform() <= taxa_crossover:
        corte = r.randint(1, len(pai1) - 1)

        filho1 = np.concatenate((pai1.rainhas[:corte], pai2.rainhas[corte:]))
        filho2 = np.concatenate((pai2.rainhas[:corte], pai1.rainhas[corte:]))

        filho1, filho2 = Tabuleiro(binario=True, rainhas=filho1), Tabuleiro(binario=True, rainhas=filho2)
        filhos = [filho1, filho2]
    else:
        filhos = [pai1, pai2]

    return filhos


# noinspection SpellCheckingInspection
def novo_cruzamento(populacao, taxa_crossover):
    nova_populacao, tamanho_populacao = [], len(populacao)
    n_rodadas = np.ceil(tamanho_populacao / 2).astype(np.int_)

    for _ in range(n_rodadas):
        pai1, pai2 = r.sample(populacao, 2)
        pai1, pai2 = pai1.rainhas, pai2.rainhas

        if np.random.uniform() <= taxa_crossover:
            corte = r.randint(1, len(pai1) - 1)

            filho1 = np.concatenate((pai1[:corte], pai2[corte:]))
            filho2 = np.concatenate((pai2[:corte], pai1[corte:]))
        else:
            filho1, filho2 = pai1, pai2

        filho1, filho2 = Tabuleiro(binario=True, rainhas=filho1), Tabuleiro(binario=True, rainhas=filho2)

        if tamanho_populacao - len(nova_populacao) >= 2:
            nova_populacao.extend([filho1, filho2])
        else:
            nova_populacao.append(filho1 if np.random.uniform() <= .5 else filho2)

    return nova_populacao


# Mutação com permutação com posição aleatória
# noinspection SpellCheckingInspection
def mutacao(pais, taxa_mutacao):
    if np.random.uniform() <= taxa_mutacao:
        tam = len(pais[0])

        for filho in pais:
            index1 = r.randint(0, tam - 1)
            index2 = r.randint(0, tam - 1)

            rainhas = filho.rainhas
            rainhas[index1], rainhas[index2] = rainhas[index2], rainhas[index1]
            filho.rainhas = rainhas

    return pais


# noinspection SpellCheckingInspection
def nova_mutacao(populacao, taxa_mutacao):
    nova_populacao, tamanho_populacao = [], len(populacao)

    for i in range(tamanho_populacao):
        rainhas = populacao[i].rainhas

        for bit in range(rainhas.ravel().shape[0]):
            if np.random.uniform() <= taxa_mutacao:
                rainhas.ravel()[bit] = not rainhas.ravel()[bit]

        novo_tabuleiro = Tabuleiro(binario=True, rainhas=rainhas)

        nova_populacao.append(novo_tabuleiro)

    return nova_populacao


# noinspection SpellCheckingInspection
def mutacao2(filhos, taxa_mutacao):
    for filho in filhos:
        rainhas = filho.rainhas

        for rainha in range(len(rainhas)):
            if np.random.uniform() <= taxa_mutacao:
                rainhas[rainha] = np.random.choice(np.array([np.True_, np.False_]), rainhas.shape[1])

        filho.rainhas = rainhas

    return filhos


# Retorna os melhores indivíduos da população antiga e da nova
# noinspection SpellCheckingInspection
def seleciona_sobreviventes(populacao, nova_populacao):
    sobreviventes = sorted(populacao + nova_populacao)

    return sobreviventes[:len(populacao)]


# noinspection SpellCheckingInspection
def seleciona_sobreviventes2(populacao, nova_populacao):
    # NÃO USAR: A ATIVIDADE NÃO PERMITE ALTERAR ESTE OPERADOR.
    sobreviventes_pais = sorted(populacao)
    sobreviventes_filhos = sorted(nova_populacao)

    comprimento_populacao = len(populacao)
    metade = int(comprimento_populacao // 2)

    if comprimento_populacao % 2 == 0:
        return sorted(sobreviventes_pais[:metade] + sobreviventes_filhos[:metade])
    else:
        return sorted(sobreviventes_pais[:metade] + sobreviventes_filhos[:metade + 1])
