# -*- encoding: utf-8 -*-
# 1. Crie uma classe derivada de lista com um metodo retorne os elementos da lista sem 
# repetição

class Lista(list):
    
    def set_list(self):
        set_ = set(self)
        
        return list(set_)