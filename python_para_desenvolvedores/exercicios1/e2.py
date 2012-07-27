# -*- encoding: utf-8 -*-
# 2. Implementar uma função que retorne verdadeiro se o número for primo (falso caso
# contrário). Testar de 1 a 100.

def isPrimo(number = 0):
    for num in range(1,100):
        if number%num == 0 & number != num & number != 1:
            return False
    return True