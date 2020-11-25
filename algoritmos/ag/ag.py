from .caixinha import *


def algoritmo_genetico(tamanho_popul, n_max_geracoes, taxa_mutacao, taxa_crossover, verboso=False, teste=False):

    popul = gera_popul_inicial(tamanho_popul)

    if teste is True:
        dados_teste = []


    for i in range(n_max_geracoes):
        nova_popul = []


        if teste is True:
            continue

        if popul[0].valor == 0:
            break

        while len(nova_popul) < tamanho_popul-1:
            pai1, pai2 = selecao_dos_pais(popul), selecao_dos_pais(popul)
            filhos = cruzamento(pai1, pai2, taxa_crossover)
            filhos = mutacao(filhos, taxa_mutacao)

            for filho in filhos: # otimizar essas coisas aqui
                nova_popul.append(filho)
            
        popul = seleciona_sobreviventes(popul, nova_popul)
        
    return popul[0] if not teste else [popul[0], dados_teste]