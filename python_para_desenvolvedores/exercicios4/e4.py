# -*- encoding: utf-8 -*-
# 4. Implementar uma classe Vetor:
# - Com coordenadas x, y e z.
# - Que suporte soma, subtração, produto escalar, produto vetorial.
# - Que calcule o módulo (valor absoluto) do vetor.

import math

class Vetor(list):
    
    
    def __add__(self, *args, **kwargs):
        for array in args:
            for i, item in enumerate(array):
                self[i] += item
        
        return self
    
    def __sub__(self, *args):
        for array in args:
            for i, item in enumerate(array):
                self[i] -= item
                
        return self
    
    def __mul__(self, *args, **kwargs):
        produto_escalar = 0
        for array in args:
            for i, item in enumerate(array):
                self[i] *= item
                produto_escalar += self[i]
                
        return produto_escalar
    
    def __pow__(self, *args):
        pass
    
    def mod(self):
        modulo = 0
        for item in self:
            modulo += item**2
        
        return round(math.sqrt(modulo), 2)
            