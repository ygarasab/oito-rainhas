from algoritmos import shc
from tabuleiro import Tabuleiro

tab1 = Tabuleiro(4)
tab2 = Tabuleiro(4)
tab1.rainhas = [2, 1, 2, 1] # exemplos do slide 12 só pra testar se tá calculando certo o valor
tab2.rainhas = [2, 0, 2, 1]
tab1.calcula_valor()
tab2.calcula_valor()
print(f"Valor do tab1: {tab1.valor}  Valor do tab2: {tab2.valor}")

shc.simulated_annealing(100)
