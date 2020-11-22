import typing as t


# noinspection SpellCheckingInspection
def verifica_tipo(**parametros):
    for parametro in parametros.keys():
        valor, descricao, tipos = parametros[parametro]

        if tipos == t.SupportsInt and not isinstance(valor, tipos):
            raise TypeError(f"O {descricao} {parametro} precisa receber um número inteiro ou um objeto que possa ser "
                            f"convertido para tal.")

        if tipos == t.SupportsFloat and not isinstance(valor, tipos):
            raise TypeError(f"O {descricao} {parametro} precisa receber um número de ponto flutuante ou um objeto que "
                            f"possa ser convertido para tal.")

        if not isinstance(valor, tipos):
            raise TypeError(f"O {descricao} {parametro} precisa receber um objeto de classe {tipos} ou que herde "
                            f"delas.")


# noinspection SpellCheckingInspection
def verifica_nao_negatividade(**parametros):
    for parametro in parametros.keys():
        valor, descricao = parametros[parametro]

        if valor < 0:
            raise ValueError(f"O {descricao} {parametro} precisa receber um número não-negativo.")
