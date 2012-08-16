'''
Created on 15/08/2012

@author: fillipecordeiro
'''
import unittest
from exercicios4.e4 import Vetor


class Test(unittest.TestCase):


    def test__add__(self):
        vetor = Vetor([1,2,3])
        vetor1 = Vetor([4,5,6])
        
        self.assertItemsEqual([5,7,9], vetor + vetor1)

    def test__sub__(self):
        vetor = Vetor([1,2,3])
        vetor1 = Vetor([4,5,6])
        
        self.assertItemsEqual([-3,-3,-3], vetor - vetor1)
        
    def test__mul__(self):
        vetor = Vetor([1,2,3])
        vetor1 = Vetor([4,5,6])
        
        self.assertEqual(32, vetor * vetor1)
        
    def test_mod(self):
        vetor = Vetor([1,2,3])
        
        self.assertEqual(3.74, vetor.mod())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test__add__']
    unittest.main()