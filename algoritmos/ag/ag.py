from .caixinha import *


def algoritmo_genetico(tamanho_popul, n_max_geracoes, taxa_mutacao, taxa_crossover, verboso=False, teste=False):

    popul = inicializa_populacao(tamanho_popul)

    if teste is True:
        dados_teste = []

    for i in range(n_max_geracoes):

        if teste is True:
            continue

        if popul[0].valor == 0:
            break
                
        nova_popul = gera_nova_populacao(popul, tamanho_popul, taxa_crossover, taxa_mutacao)
            
        popul = seleciona_sobreviventes(popul, nova_popul)

    return popul[0] if not teste else [popul[0], dados_teste]