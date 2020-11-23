from algoritmos import shc
from algoritmos.tabuleiro import Tabuleiro

tab1 = Tabuleiro(4)
tab2 = Tabuleiro(4)
tab1.rainhas = [2, 1, 2, 1]  # exemplos do slide 12 pra testar se tá calculando o valor certo
tab2.rainhas = [2, 0, 2, 1]

print(f"Valor do tab1: {tab1.valor}\n"
      f"Valor do tab2: {tab2.valor}")

# noinspection SpellCheckingInspection
tabuleiro = shc.simulated_annealing(100, .01)
