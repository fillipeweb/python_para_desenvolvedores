# -*- encoding: utf-8 -*-
# 1. Implementar um gerador de números primos.

def gen_primos():
    
    numeros = [2] + range(3,1001,2)
    primos = [] 
    for i in numeros:
        if sum([ 1 for div in range(2,i) if i % div == 0 ]) == 0:
            primos.append(i)
                
    return primos
    
if __name__ == "__main__":
    print gen_primos()
