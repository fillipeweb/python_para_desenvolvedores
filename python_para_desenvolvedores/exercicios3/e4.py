# -*- encoding: utf-8 -*-
# 4. Implementar um gerador que leia um arquivo e retorne uma lista de tuplas com os
# dados (o separador de campo do arquivo é vírgula), eliminando as linhas vazias. Caso
# ocorra algum problema, imprima uma mensagem de aviso e encerre o programa.

import traceback

def gen_file(file_ = None):
    temp = file(file_)
    try:
        for line in temp.readlines():
            line = line.strip()
            if line:
                yield eval('(' + line + ')')
    except:
        trace = traceback.format_exc()
        print 'Aconteceu um erro:\n', trace
        raise SystemExit
    
if __name__ == "__main__":
    for i in gen_file('file.e4'):
        print i