from .operadores import *
from .caixinha import *


# noinspection SpellCheckingInspection
def algoritmo_genetico(tamanho_populacao=20, max_iteracoes=1000, taxa_mutacao=.03, taxa_crossover=.8, verboso=False):
    pais = inicializa_populacao(tamanho_populacao)
    iteracao = 0

    if verboso is True:
        print(f"[Iteração {iteracao}] População inicial: \n"
              f"{gera_contagem_populacao(pais)}", end="\n\n")

    while iteracao < max_iteracoes:

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

    if iteracao >= max_iteracoes and verboso is True:
        print("O número máximo de iterações foi atingido.")

    # noinspection PyUnboundLocalVariable
    # return pais[0] if not teste else [pais[0], dados_teste]
    return pais[0], iteracao
