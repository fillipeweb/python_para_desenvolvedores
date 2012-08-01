# -*- encoding: utf-8 -*-
# 2. Implementar um módulo com duas funções:
# ▪ matrix_sum(*matrices), que retorna a matriz soma de matrizes de duas dimensões.
# ▪ camel_case(s), que converte nomes para CamelCase.

def matrix_sum(*matrices):
    matrix_soma = []
    for matrix in matrices:
        for i,item in enumerate(matrix):
            try:
                matrix_soma[i] = matrix_soma[i] + item
            except IndexError:
                matrix_soma.append(item)
    return matrix_soma

def camel_case(s):
    sOut = ''
    for s1 in s.split(u'\u0020'):
        sOut += s1.capitalize()
    return sOut