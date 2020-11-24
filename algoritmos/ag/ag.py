from .caixinha import *


def algoritmo_genetico(tamanho_popul, n_max_geracoes, taxa_mutacao, taxa_crossover, verboso=False, teste=False):

    popul = gera_popul_inicial(tamanho_popul)
    if teste is True:
        dados_teste = []

    for i in range(n_max_geracoes):

        if teste is True:

            continue

        if popul[0] == 0:
            break

        nova_popul = popul.copy()
        nova_popul = cruza_filhos(nova_popul, taxa_crossover)
        nova_popul = muta_filhos(nova_popul, taxa_mutacao)

        popul = seleciona_sobreviventes(popul, nova_popul)

    return popul[0] if not teste else [popul[0], dados_teste]
