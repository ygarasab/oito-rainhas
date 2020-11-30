import algoritmos
import experimentos

tab1 = algoritmos.Tabuleiro(n_rainhas=4)
tab2 = algoritmos.Tabuleiro(n_rainhas=4)
tab1.rainhas = [2, 1, 2, 1]  # exemplos do slide 12 pra testar se tá calculando o valor certo
tab2.rainhas = [2, 0, 2, 1]

print(f"Valor do tab1: {tab1.valor}\n"
      f"Valor do tab2: {tab2.valor}")

# noinspection SpellCheckingInspection
# tabuleiro = algoritmos.shc.simulated_annealing(100, .01, True)

# print(tabuleiro)

# ag1 = algoritmos.ag.algoritmo_genetico(20, 1000, .03, .8, True)  # conforme pedido pelo professor
# print(ag1)

resultados, figura = experimentos.executa_experimentos(algoritmos.shc.simulated_annealing, 50)
# resultados, figura = experimentos.executa_experimentos(algoritmos.ag.algoritmo_genetico, 50)

figura.show()
