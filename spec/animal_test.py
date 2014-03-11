#coding: utf-8
import unittest
from should_dsl import should
from sistema_veterinario.animal import Animal
from sistema_veterinario.especie import Especie
from sistema_veterinario.consulta import Consulta
from sistema_veterinario.veterinario import Veterinario

#Testes com a classe Animal
class AnimalTest(unittest.TestCase):

	def test_criar_animal(self):
		especie = Especie(20, "Mamífero")

		animal = Animal(10, "Cachorro", "Macho", especie.nome)
		animal.codAnimal |should| equal_to (10)
		animal.nome |should| equal_to ("Cachorro")
		animal.sexo |should| equal_to ("Macho")
		animal.especie |should| equal_to (especie.nome)

	def test_fazer_update_animal(self):
		especie = Especie(20, "Mamífero")
		especie2 = Especie(50, "Felino")

		animal = Animal(10, "Cachorro", "Macho", especie.nome)
		animal.nome |should| equal_to ("Cachorro")

		animal.fazer_update("Gato", especie2.nome)
		animal.nome |should| equal_to ("Gato")
		animal.especie |should| equal_to(especie2.nome)

	def test_inserir_lista_consultas(self):
		especie = Especie(20, "Mamífero")
		veterinario = Veterinario(5, "Marcelo", "102102121")
		animal = Animal(10, "Cachorro", "Macho", especie.nome)   

		consulta = Consulta(1, "12/12/2012", veterinario.nome, animal.nome, "Resumo")
		consulta2= Consulta(2, "24/12/2012", veterinario.nome, animal.nome, "Resumo 2")
		
		animal.inserir_lista_consultas(consulta)
		animal.inserir_lista_consultas(consulta2)

		(consulta in animal.lista_consultas) |should| equal_to(True) 
		(consulta2 in animal.lista_consultas) |should| equal_to(True) 