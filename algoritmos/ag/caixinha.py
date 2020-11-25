from ..tabuleiro import Tabuleiro
import random
import numpy as np


def inicializa_populacao(tamanho_popul):
    popul = [Tabuleiro() for _ in range(tamanho_popul)]

    return rankea_populacao(popul)

def rankea_populacao(popul):    
    return sorted(popul)

def gera_nova_populacao(popul, tamanho_popul, taxa_crossover, taxa_mutacao):
    nova_popul = []

    while len(nova_popul) < tamanho_popul:       
        pais = selecao_dos_pais(popul)
        filhos = cruzamento(pais, taxa_crossover)
        filhos = mutacao(filhos, taxa_mutacao)
        nova_popul.extend(filhos)

    return rankea_populacao(nova_popul)

# 3-Way Tournament Selection: selecionamos 3 indivíduos aleatórios da população para "lutar" entre si e ganha o que tiver melhor fitness.
def selecao_dos_pais(popul): 
    pais = []

    for _ in range(2):
        lutadores = random.sample(popul, 3) 
        lutadores = rankea_populacao(lutadores)
        
        if lutadores[0] in pais:
            pais.append(lutadores[1])
        else:
            pais.append(lutadores[0])

    return pais

# Cruzamento com ponto de corte aleatório
def cruzamento(pais, taxa_crossover):
    pai1 = pais[0]
    pai2 = pais[1]

    n = len(pai1)
    c = random.randint(0, n-1)

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
def mutacao(filhos, taxa_mutacao):
    if np.random.uniform() <= taxa_mutacao:
        tam = len(filhos[0])
    
        for filho in filhos:
            index1 = random.randint(0, tam-1)
            index2 = random.randint(0, tam-1)

            filho.rainhas[index1], filho.rainhas[index2] = filho.rainhas[index2], filho.rainhas[index1] 

    return filhos

# Retorna os melhores indivíduos da população antiga e da nova
def seleciona_sobreviventes(popul, nova_popul):
    sobreviventes = rankea_populacao(popul + nova_popul)
    
    return sobreviventes[:len(popul)]