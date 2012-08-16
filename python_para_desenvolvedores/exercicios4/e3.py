# -*- encoding: utf-8 -*-
# 1. Implemente uma classe Carro com as seguintes propriedades:
# - Um veiculo tem um certo consumo de combustivel (medido em km / litro) e uma
# certa quantidade de combustivel no tanque.
# - O consumo é especificado no construtor e o nivel de combustivel inicial é 0.
# - Forneça o metodo mover(km) que recebe uma distancia em quilometros e reduza o 
# nivel de combustivel no tanque de gasolina.
# - Forneça um metodo gasolina(), que retorna o nivel atual de combustivel.
# - Forneça um metodo abastecer(litros), para abastecer o tanque.

class Carro(object):
    
    
    def __init__(self, consumo, combustivel = 0.0):
        self.consumo = consumo
        self.combustivel = combustivel
        
    def mover(self, distancia):
        self.combustivel -= round(float(distancia / self.consumo),2)
    
    def gasolina(self):
        return self.combustivel
    
    def abastecer(self, litros):
        self.combustivel += litros
        