import unittest

import coletando_autores

class ReqTest(unittest.TestCase):

    def teste_autores(self):
        esperado = 'Albert Einstein'
        atual = coletando_autores.coletando_primeiro_autores()

        self.assertEqual(esperado, atual)