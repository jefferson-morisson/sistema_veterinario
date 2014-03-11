#coding: utf-8
import unittest
from should_dsl import should
from sistema_veterinario.veterinario import Veterinario
from sistema_veterinario.especie import Especie
from sistema_veterinario.consulta import Consulta
from sistema_veterinario.animal import Animal

#Testes com a classe Veterinário
class VeterinarioTest(unittest.TestCase):

	def test_criar_veterinario(self):
		veterinario = Veterinario(5, "Marcelo", "102102121")
		veterinario.codVeterinario |should| equal_to(5)
		veterinario.nome |should| equal_to("Marcelo")
		veterinario.crmv |should| equal_to("102102121")

	def test_fazer_update(self):
		veterinario = Veterinario(5, "Marcelo", "102102121")
		veterinario.fazer_update("Carlos", "454572")
		veterinario.nome |should| equal_to("Carlos")
		veterinario.crmv |should| equal_to("454572")
		
	def test_inserir_lista_consultas(self):
		especie = Especie(20, "Mamífero")
		animal = Animal(10, "Cachorro", "Macho", especie.nome)   
		veterinario = Veterinario(5, "Marcelo", "102102121")

		consulta = Consulta(1, "12/12/2012", veterinario.nome, animal.nome, "Resumo")
		consulta2 = Consulta(2, "24/12/2012", veterinario.nome, animal.nome, "Resumo 2")
		
		veterinario.inserir_lista_consultas(consulta)
		veterinario.inserir_lista_consultas(consulta2)

		(consulta in veterinario.lista_consultas) |should| equal_to(True) 
		(consulta2 in veterinario.lista_consultas) |should| equal_to(True) 