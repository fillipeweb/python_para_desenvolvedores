# -*- encoding: utf-8 -*-
# 1. Crie uma classe que modele um quadrado, com uma tribuito lado e os metodos: mudar 
# valor do lado, retornar valor do lado e calcular area.

class Quadrado(object):
    
    def __init__(self, lado):
        self.lado = lado
    
    def mudar_valor_lado(self, lado):
        self.lado = lado
        
    def pegar_valor_lado(self):
        return self.lado
    
    def calcular_area(self):
        return self.lado * self.lado