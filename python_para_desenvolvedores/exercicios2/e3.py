# -*- encoding: utf-8 -*-
# 3. Implementar uma função que leia um arquivo e retorne uma lista de tuplas com os
# dados (o separador de campo do arquivo é vírgula), eliminando as linhas vazias. Caso
# ocorra algum problema, imprima uma mensagem de aviso e encerre o programa.
import traceback

def get_data_from_file(file_ = None):
    temp = file(file_)
    tuple_list = []
    try:
        for line in temp.readlines():
            line = line.strip()
            if line:
                tuple_list.append(eval('(' + line + ')'))
    except:
        trace = traceback.format_exc()
        print 'Aconteceu um erro:\n', trace
        raise SystemExit
            
    return tuple_list