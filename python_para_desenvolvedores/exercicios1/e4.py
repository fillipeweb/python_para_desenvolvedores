# -*- encoding: utf-8 -*-
# 4. Implementar uma função que receba um dicionário e retorne a soma, a média e a
# variação dos valores.

def dictStat(dict_ = {}):
    sum_ = 0
    for value in dict_:
        sum_ += value
    average = sum_/len(dict_)
    
    print u'Dicionário: %s \nSoma: %d \nMédia: %d' % (dict_, sum_, average)