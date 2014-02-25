#coding: utf-8
import unittest
from should_dsl import should
from sistema_veterinario.veterinario import Veterinario

#Testes com a classe Veterinário
class VeterinarioTest(unittest.TestCase):

	def test_criar_veterinario(self):
		veterinario = Veterinario(5, "Marcelo", "102102121")
		veterinario.codVeterinario |should| equal_to(5)
		veterinario.nome |should| equal_to("Marcelo")
		veterinario.crmv |should| equal_to("102102121")