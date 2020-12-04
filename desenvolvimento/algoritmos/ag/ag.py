import numpy as np
import typing as t

from . import caixinha
from . import operadores
from .. import checagens


# noinspection SpellCheckingInspection
def algoritmo_genetico(tamanho_populacao=20, max_iteracoes=1000, taxa_mutacao=.03, taxa_crossover=.8,
                       tamanho_ringue=3, verboso=False):
    tamanho_populacao = checagens.verifica_tipo(tamanho_populacao=(tamanho_populacao, "parâmetro", t.SupportsInt))
    max_iteracoes = checagens.verifica_tipo(max_iteracoes=(max_iteracoes, "parâmetro", t.SupportsInt))
    taxa_mutacao = checagens.verifica_tipo(taxa_mutacao=(taxa_mutacao, "parâmetro", t.SupportsFloat))
    taxa_crossover = checagens.verifica_tipo(taxa_crossover=(taxa_crossover, "parâmetro", t.SupportsFloat))
    tamanho_ringue = checagens.verifica_tipo(tamanho_do_ringue=(tamanho_ringue, "parâmetro", t.SupportsInt))
    verboso = checagens.verifica_tipo(verboso=(verboso, "parâmetro", (bool, np.bool_)))

    checagens.verifica_nao_negatividade(tamanho_populacao=(tamanho_populacao, "parâmetro"),
                                        max_iteracoes=(max_iteracoes, "parâmetro"),
                                        taxa_mutacao=(taxa_mutacao, "parâmetro"),
                                        taxa_crossover=(taxa_crossover, "parâmetro"),
                                        tamanho_ringue=(tamanho_ringue, "parâmetro"))

    checagens.verifica_menor_ou_igual_a(taxa_mutacao=(taxa_mutacao, "parâmetro"), valor=(1, "valor"))
    checagens.verifica_menor_ou_igual_a(taxa_mutacao=(taxa_crossover, "parâmetro"), valor=(1, "valor"))
    checagens.verifica_menor_ou_igual_a(tamanho_ringue=(tamanho_ringue, "parâmetro"),
                                        tamanho_populacao=(tamanho_populacao, "parâmetro"))

    pais = operadores.inicializa_populacao(tamanho_populacao)
    iteracao = 0

    if verboso is True:
        print(f"[Iteração {iteracao}] População inicial: \n"
              f"{caixinha.gera_contagem_populacao(pais)}", end="\n\n")

    while iteracao < max_iteracoes:
        if pais[0].valor == 0:
            if verboso is True:
                print("Uma solução ótima foi encontrada.")

            break

        filhos = operadores.nova_gera_nova_populacao(pais, taxa_crossover, taxa_mutacao, tamanho_ringue)
        pais = operadores.seleciona_sobreviventes(pais, filhos)
        iteracao += 1

        if verboso is True:
            print(f"[Iteração {iteracao}]\n"
                  f"Filhos: \n"
                  f"{caixinha.gera_contagem_populacao(filhos)}\n\n"
                  f"Sobreviventes: \n"
                  f"{caixinha.gera_contagem_populacao(pais)}", end="\n\n")

    if iteracao >= max_iteracoes and verboso is True:
        print("O número máximo de iterações foi atingido.")

    return pais[0], iteracao
