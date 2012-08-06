# -*- encoding: utf-8 -*-
# 6. Faça um script que:
# ▪ Leia um arquivo texto.
# ▪ Conte as ocorrências de cada palavra.
# ▪ Mostre os resultados ordenados pelo número de ocorrências.

def word_stat(file_ = None):
    temp = file(file_)
    word_hash = {}
    for s in temp.readlines():
        array = s.split(u'\u0020')
        for a in array:
            if word_hash.has_key(a):
                word_hash[a] = word_hash[a] + 1
            else:
                word_hash[a] = 1     
    
    return sorted(word_hash.iteritems(), key=lambda (k,v): (v,k), reverse = True)