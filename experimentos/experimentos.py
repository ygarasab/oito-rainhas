import numpy as np
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt
from timeit import default_timer as timer


# noinspection SpellCheckingInspection
def executa_experimentos(funcao, n_execucoes=50, verbose=True):
    melhores_solucoes = np.empty((n_execucoes, 1), dtype=np.object_)
    melhores_valores = np.empty((n_execucoes, 1), dtype=np.int_)
    tempos_gastos = np.empty((n_execucoes, 1), dtype=np.float_)
    iteracoes_gastas = np.empty((n_execucoes, 1), dtype=np.int_)

    for e in range(n_execucoes):
        if verbose is True:
            print(f"Execução {e + 1}...", end="\r")

        tempos_gastos[e, 0] = timer()
        melhores_solucoes[e, 0], iteracoes_gastas[e, 0] = funcao()
        tempos_gastos[e, 0] = timer() - tempos_gastos[e, 0]
        melhores_valores[e, 0] = melhores_solucoes[e, 0].valor
        melhores_solucoes[e, 0] = str(melhores_solucoes[e, 0])

    resultados = np.concatenate((melhores_solucoes, melhores_valores, tempos_gastos, iteracoes_gastas), axis=1)
    resultados = pd.DataFrame(resultados, columns=["Solução", "Função-objetivo", "Tempo", "Iterações"]).infer_objects()

    figure, axes = plt.subplots(1, 2, figsize=(10, 5))

    figure.suptitle(f"Dados da execução do algoritmo {str(funcao).split(' ')[1]}")

    axes[0].set_title("Iterações mínimas por execução")
    axes[1].set_title("Tempo mínimo por execução")

    sns.lineplot(x=range(1, n_execucoes + 1), y=iteracoes_gastas.ravel(), ax=axes[0])
    sns.lineplot(x=range(1, n_execucoes + 1), y=tempos_gastos.ravel(), ax=axes[1])

    if verbose is True:
        print(f"Execução concluída.")

    return resultados, figure
