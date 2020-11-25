from ..tabuleiro import Tabuleiro
import operator
import random
import numpy as np


def gera_popul_inicial(tamanho_popul):
    popul = []
    for _ in range(tamanho_popul):
        popul.append(Tabuleiro())

    popul = rankea_populacao(popul)
    
    return popul

def rankea_populacao(popul):    
    popul = sorted(popul, key=lambda individuo: individuo.valor)

    return popul

# 3-Way Tournament Selection: selecionamos 3 indivíduos aleatórios da população para "lutar" entre si e ganha o que tiver melhor fitness.
def selecao_dos_pais(popul): 
    lutadores = []

    for _ in range(3):
        lutadores.append(random.choice(popul))

    lutadores = rankea_populacao(lutadores)
    
    return lutadores[0]

# Cruzamento com ponto de corte aleatório
def cruzamento(pai1, pai2, taxa_crossover):
    n = len(pai1)
    c = random.randint(0, n-1)

    if np.random.uniform() <= taxa_crossover:
        filho1 = Tabuleiro()
        filho1.rainhas = np.concatenate((pai1.rainhas[0:c], pai2.rainhas[c:n]), axis=None)

        filho2 = Tabuleiro()
        filho2.rainhas = np.concatenate((pai2.rainhas[0:c], pai1.rainhas[c:n]), axis=None)
        filhos = [filho1, filho2]
    else:
        filhos = [pai1, pai2]

    return filhos

# Mutação com permutação com posição aleatória
def mutacao(popul, taxa_mutacao):
    if np.random.uniform() <= taxa_mutacao:
        tam = len(popul)
        index1 = random.randint(0, tam-1)
        index2 = random.randint(0, tam-1)

        for individuo in popul:
            aux = individuo.rainhas[index1]
            individuo.rainhas[index1] = individuo.rainhas[index2]
            individuo.rainhas[index2] = aux

    return popul

# Conserva o individuo com melhor fitness da população e adiciona os individuos da nova população
def seleciona_sobreviventes(popul, nova_popul):
    sobreviventes = [popul[0]]

    for individuo in nova_popul:
        sobreviventes.append(individuo)
    
    return rankea_populacao(sobreviventes)