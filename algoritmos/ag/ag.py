from .operadores import *
from .caixinha import *


# noinspection SpellCheckingInspection
def algoritmo_genetico(tamanho_populacao, max_iteracoes, taxa_mutacao, taxa_crossover, verboso=False, teste=False):
    pais = inicializa_populacao(tamanho_populacao)
    iteracao = 0

    if teste is True:
        dados_teste = []

    if verboso is True:
        print(f"[Iteração {iteracao}] População inicial: \n"
              f"{gera_contagem_populacao(pais)}", end="\n\n")

    while iteracao < max_iteracoes:
        if teste is True:
            continue

        if pais[0].valor == 0:
            if verboso is True:
                print("Uma solução ótima foi encontrada.")

                break

        filhos = gera_nova_populacao(pais, tamanho_populacao, taxa_crossover, taxa_mutacao)
        pais = seleciona_sobreviventes(pais, filhos)
        iteracao += 1

        if verboso is True:
            print(f"[Iteração {iteracao}]\n"
                  f"Filhos: \n"
                  f"{gera_contagem_populacao(filhos)}\n\n"
                  f"Sobreviventes: \n"
                  f"{gera_contagem_populacao(pais)}", end="\n\n")

    # noinspection PyUnboundLocalVariable
    return pais[0] if not teste else [pais[0], dados_teste]
