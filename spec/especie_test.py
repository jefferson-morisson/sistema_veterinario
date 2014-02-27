#coding: utf-8
import unittest
from should_dsl import should
from sistema_veterinario.especie import Especie

#Testes com a classe Especie
class EspecieTest(unittest.TestCase):
	
	def test_criar_especie(self):
		especie = Especie(1, "Mamífero")
		especie.codEspecie |should| equal_to(1)
		especie.nome |should| equal_to("Mamífero")