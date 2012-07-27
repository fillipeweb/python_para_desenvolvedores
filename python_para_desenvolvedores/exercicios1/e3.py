# -*- encoding: utf-8 -*-
# 3. Implementar uma função que receba uma lista de listas de comprimentos quaisquer e
# retorne uma lista de uma dimensão.

def linkList(**kargs):
    listOut = []
    for lists in kargs:
        for item in lists:
            listOut.append(item)