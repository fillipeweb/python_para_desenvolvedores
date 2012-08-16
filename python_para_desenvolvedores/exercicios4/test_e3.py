'''
Created on 13/08/2012

@author: fillipecordeiro
'''
import unittest
from exercicios4.e3 import Carro


class Test(unittest.TestCase):


    def test_gasolina(self):
        carro = Carro(1.5, 10)
        self.assertEqual(carro.gasolina(), 10)
    
    def test_abastecer(self):
        carro = Carro(1.5)
        carro.abastecer(5)
        self.assertEqual(carro.gasolina(), 5)
    
    def test_mover(self):
        carro = Carro(1.5, 10)
        carro.mover(2)
        self.assertEqual(carro.gasolina(), 8.67)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_mover']
    unittest.main()