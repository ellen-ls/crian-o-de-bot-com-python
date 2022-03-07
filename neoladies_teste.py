import unittest

import neoladies

class ReqTest(unittest.TestCase):

    def teste_primeira_frase(self):
        esperado = '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
        atual = neoladies.coletando_primeira_frase()

        self.assertEqual(esperado, atual)







#import unittest

#import neoladies

#class ReqTest(unittest.TestCase):

    #def teste_priemira_frase(self):
        #esperado = '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
        #atual = neoladies.coletando_primeira_frase()

        #self.assertEqual(esperado, atual)
        
