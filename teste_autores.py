import unittest

import coletando_autores

from bs import beauty4



class ReqTest(unittest.TestCase):

    def teste_autores(self):
        esperado = 'Albert Einstein'
        atual = coletando_autores.coletando_primeiro_autores()

        self.assertEqual(esperado, atual)
        
        
    
    
    