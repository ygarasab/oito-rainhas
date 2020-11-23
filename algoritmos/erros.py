import numpy as np
import typing as t


# noinspection SpellCheckingInspection
def verifica_tipo(**parametro_dict):
    if len(parametro_dict.keys()) != 1:
        raise ValueError("Apenas um argumento pode ser passado para esta função.")

    # noinspection PyUnresolvedReferences
    parametro = list(parametro_dict.keys())[0]
    valor, descricao, tipos = parametro_dict[parametro]

    if tipos == t.SupportsFloat and not isinstance(valor, tipos):
        if not isinstance(valor, tipos):
            raise TypeError(f"O {descricao} {parametro} precisa receber um número de ponto flutuante ou um objeto que "
                            f"possa ser convertido para tal.")
        else:
            return float(valor)

    if tipos == t.SupportsInt:
        if not isinstance(valor, tipos):
            raise TypeError(f"O {descricao} {parametro} precisa receber um número inteiro ou um objeto que possa ser "
                            f"convertido para tal.")
        else:
            return int(valor)

    if tipos == np.ndarray:
        if not isinstance(valor, np.ndarray):
            if not isinstance(valor, (list, tuple)):
                raise TypeError(f"O {descricao} {parametro} precisa receber um array numpy ou um objeto que possa ser "
                                f"convertido para tal.")
            else:
                return np.array(valor)

    if not isinstance(valor, tipos):
        raise TypeError(f"O {descricao} {parametro} precisa receber um objeto de classe {tipos} ou que herde delas.")
    else:
        return valor


# noinspection SpellCheckingInspection
def verifica_tipo_operador(operador, valor, tipo):
    if not isinstance(valor, tipo):
        raise TypeError(f"O operador '{operador}' precisa ser do tipo {tipo}.")


# noinspection SpellCheckingInspection
def verifica_nao_negatividade(**parametros):
    for parametro in parametros.keys():
        valor, descricao = parametros[parametro]

        if valor < 0:
            raise ValueError(f"O {descricao} {parametro} precisa receber um número não-negativo.")


# noinspection SpellCheckingInspection
def verifica_ndim(**parametros):
    for parametro in parametros.keys():
        valor, descricao, ndim = parametros[parametro]

        if valor.ndim != ndim:
            raise ValueError(f"O o atributo ndim do {descricao} {parametro} precisa ser igual a {ndim}.")


# noinspection SpellCheckingInspection
def verifica_maior_ou_igual_a(**parametros):
    if len(parametros.keys()) != 2:
        raise ValueError("Apenas dois argumentos podem ser passados para esta função.")

    parametro, outro_parametro = parametros.keys()

    valor, descricao = parametros[parametro]
    outro_valor, outra_descricao = parametros[outro_parametro]

    if outro_valor is not None and valor < outro_valor:
        raise ValueError(f"O {descricao} {parametro} precisa receber um valor, no mínimo, igual ao {outra_descricao} "
                         f"{outro_parametro}.")


# noinspection SpellCheckingInspection
def verifica_menor_ou_igual_a(**parametros):
    if len(parametros.keys()) != 2:
        raise ValueError("Apenas dois argumentos podem ser passados para esta função.")

    parametro, outro_parametro = parametros.keys()

    valor, descricao = parametros[parametro]
    outro_valor, outra_descricao = parametros[outro_parametro]

    if outro_valor is not None and valor > outro_valor:
        raise ValueError(f"O {descricao} {parametro} precisa receber um valor, no máximo, igual ao {outra_descricao} "
                         f"{outro_parametro}.")


# noinspection SpellCheckingInspection
def verifica_comprimento_maior_ou_igual_a(**parametros):
    if len(parametros.keys()) != 2:
        raise ValueError("Apenas dois argumentos podem ser passados para esta função.")

    parametro, outro_parametro = parametros.keys()

    valor, descricao = parametros[parametro]
    outro_valor, outra_descricao = parametros[outro_parametro]

    if outro_valor is not None and valor.shape[0] < outro_valor:
        raise ValueError(f"O {descricao} {parametro} precisa receber um valor, no mínimo, igual ao {outra_descricao} "
                         f"{outro_parametro}.")


# noinspection SpellCheckingInspection
def verifica_comprimento_menor_ou_igual_a(**parametros):
    if len(parametros.keys()) != 2:
        raise ValueError("Apenas dois argumentos podem ser passados para esta função.")

    parametro, outro_parametro = parametros.keys()

    valor, descricao = parametros[parametro]
    outro_valor, outra_descricao = parametros[outro_parametro]

    if outro_valor is not None and valor.shape[0] > outro_valor:
        raise ValueError(f"O comprimento do {descricao} {parametro} precisa ser, no máximo, igual ao {outra_descricao} "
                         f"{outro_parametro}.")
