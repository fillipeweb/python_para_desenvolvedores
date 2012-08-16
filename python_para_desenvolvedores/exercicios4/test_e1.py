'''
Created on 13/08/2012

@author: fillipecordeiro
'''
import unittest
from exercicios4.e1 import Quadrado


class Test(unittest.TestCase):

    def test_mudar_valor_lado(self):    
        quadrado = Quadrado(0)
        quadrado.mudar_valor_lado(2)
        self.assertEqual(quadrado.pegar_valor_lado(), 2)

    def test_pegar_valor_lado(self):
        quadrado = Quadrado(1)
        self.assertEqual(quadrado.pegar_valor_lado(), 1)
        
    def test_calcular_area(self):
        quadrado = Quadrado(2)
        self.assertEqual(quadrado.calcular_area(), 4)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_mudar_valor_lado']
    unittest.main()