'''
Created on 13/08/2012

@author: fillipecordeiro
'''
import unittest
from exercicios4.e2 import Lista


class Test(unittest.TestCase):


    def test_set_listself(self):
        lista = Lista([1,2,3,4,4,5,6,6])
        self.assertEqual(len(lista.set_list()), 6)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()