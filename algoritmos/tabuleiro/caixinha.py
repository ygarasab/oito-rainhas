import numpy as np
import typing as t

from .. import checagens


# noinspection SpellCheckingInspection
def decimal_para_binario(numero, numero_de_bits):
    numero = checagens.verifica_tipo(numero=(numero, "parâmetro", t.SupportsInt))
    digitos_binarios = list(bin(numero + 1)[2:].zfill(numero_de_bits))

    checagens.verifica_comprimento_binario_igual_a(numero=(digitos_binarios, "parâmetro"),
                                                   numero_de_bits=(numero_de_bits, "parâmetro"))

    return np.array(digitos_binarios, dtype=np.int_).astype(np.bool_)


# noinspection SpellCheckingInspection
def binario_para_decimal(bits):
    bits = checagens.verifica_tipo(bits=(bits, "parâmetro", np.ndarray))

    return int("".join(bits.astype(np.int_).astype(str)), base=2) - 1


# noinspection SpellCheckingInspection
def ajusta_indentacao(string, string_para_adicionar):
    linhas = string.split("\n")

    for linha in range(1, len(linhas)):
        linhas[linha] = string_para_adicionar + linhas[linha]

    return "\n".join(linhas)
