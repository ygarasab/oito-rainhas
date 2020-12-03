import numpy as np
import pandas as pd
import seaborn as sns
import typing as t

from matplotlib import pyplot as plt
from timeit import default_timer as timer
from . import checagens


# noinspection SpellCheckingInspection
def executa_experimento(funcao, n_execucoes=50, verboso=True):
    n_execucoes = checagens.verifica_tipo(n_execucoes=(n_execucoes, "parâmetro", t.SupportsInt))
    verboso = checagens.verifica_tipo(verboso=(verboso, "parâmetro", (bool, np.bool_)))

    melhores_solucoes = np.empty((n_execucoes, 1), dtype=np.object_)
    melhores_valores = np.empty((n_execucoes, 1), dtype=np.int_)
    tempos_gastos = np.empty((n_execucoes, 1), dtype=np.float_)
    iteracoes_gastas = np.empty((n_execucoes, 1), dtype=np.int_)

    for e in range(n_execucoes):
        if verboso is True:
            print(f"Execução {e + 1}...", end="\r")

        tempos_gastos[e, 0] = timer()
        melhores_solucoes[e, 0], iteracoes_gastas[e, 0] = funcao()
        tempos_gastos[e, 0] = timer() - tempos_gastos[e, 0]
        melhores_valores[e, 0] = melhores_solucoes[e, 0].valor
        melhores_solucoes[e, 0] = str(melhores_solucoes[e, 0])

    tabela = np.concatenate((melhores_solucoes, melhores_valores, tempos_gastos, iteracoes_gastas), axis=1)
    tabela = pd.DataFrame(tabela, columns=["Solução", "Função-objetivo", "Tempo (segundos)",
                                           "Iterações"]).infer_objects()

    figura, eixos = plt.subplots(1, 2, figsize=(15, 5))

    figura.tight_layout()
    eixos[0].set_xlim(1, 50)
    eixos[1].set_xlim(1, 50)

    figura.suptitle(f"Dados da execução do algoritmo {str(funcao).split(' ')[1]}")

    eixos[0].set_title("Iterações mínimas por execução")
    eixos[1].set_title("Tempo mínimo por execução (em segundos)")

    sns.lineplot(x=range(1, n_execucoes + 1), y=iteracoes_gastas.ravel(), ax=eixos[0])
    sns.lineplot(x=range(1, n_execucoes + 1), y=tempos_gastos.ravel(), ax=eixos[1])

    if verboso is True:
        print(f"Execução concluída.")

    return tabela, figura
