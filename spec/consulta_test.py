#coding: utf-8
import unittest
from should_dsl import should
from sistema_veterinario.consulta import Consulta
from sistema_veterinario.veterinario import Veterinario
from sistema_veterinario.animal import Animal

#Testes com a classe Consulta
class ConsultaTest(unittest.TestCase):

	def test_criar_consulta(self):
		veterinario = Veterinario(5, "Marcelo", "102102121")
		animal = Animal(2, "Cachorro", "Macho", "Mamífero")

		consulta = Consulta(1, "12/12/2012", veterinario.nome, animal.nome, "Resumo")
		consulta.codConsulta |should| equal_to(1)
		consulta.data |should| equal_to("12/12/2012")

		consulta.veterinario |should| equal_to(veterinario.nome)
		consulta.animal |should| equal_to(animal.nome)
		consulta.resumoConsulta |should| equal_to("Resumo")

	def test_fazer_update(self):
		veterinario = Veterinario(5, "Marcelo", "102102121")
		animal = Animal(2, "Cachorro", "Macho", "Mamífero")
		consulta = Consulta(1, "12/12/2012", veterinario.nome, animal.nome, "Resumo")
		consulta.data |should| equal_to("12/12/2012")

		veterinario_novo = Veterinario(7, "Lucas", "444444")
		animal_novo = Animal(78, "Gato", "Macho", "Mamífero")

		consulta.fazer_update("26/10/2013", veterinario_novo.nome, animal_novo.nome, "Resumo novo")
		
		consulta.data |should| equal_to("26/10/2013")
		consulta.veterinario |should| equal_to(veterinario_novo.nome)
		consulta.animal |should| equal_to(animal_novo.nome)
		consulta.resumoConsulta |should| equal_to("Resumo novo")