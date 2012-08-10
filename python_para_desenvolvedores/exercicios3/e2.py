# -*- encoding: utf-8 -*-
# 2. Implementar o gerador de números primos como uma expressão (dica: use o módulo
# itertools).

def gen_primos():
    
    numeros = [2] + range(3,1001,2)
    primos = [] 
    for i in numeros:
        if sum([ 1 for div in range(2,i) if i % div == 0 ]) == 0:
            primos.append(i)
            yield i

if __name__ == "__main__":
    primeiro_milhao_de_primos = (i for i in gen_primos() if i < 1000000)
    for i in primeiro_milhao_de_primos:
        print i