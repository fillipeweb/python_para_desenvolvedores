# -*- encoding: utf-8 -*-
# 1. Implementar um programa que receba um nome de arquivo e gere estatísticas sobre o
# arquivo (número de caracteres, número de linhas e número de palavras)

def fileStat(_file = None):
    temp = file(_file)
    nro_caracteres = 0
    nro_palavras = 0
    nro_linhas = 0
    for s in temp.readlines():
        nro_caracteres += len(s[::])
        nro_palavras += len(s.split(u"\u0020"))
        nro_linhas += 1
    
    print 'File: %s \nNro Caracteres: %d \nNro Linhas: %d \nNro Palavras: %d' % (temp.name, nro_caracteres, nro_linhas, nro_palavras)
    