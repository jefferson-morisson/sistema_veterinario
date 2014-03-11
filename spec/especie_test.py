#coding: utf-8
import unittest
from should_dsl import should
from sistema_veterinario.especie import Especie
from sistema_veterinario.animal import Animal

#Testes com a classe Especie
class EspecieTest(unittest.TestCase):
	
	def test_criar_especie(self):
		especie = Especie(1, "Mamífero")
		especie.codEspecie |should| equal_to(1)
		especie.nome |should| equal_to("Mamífero")

	def test_fazer_update_especie(self):
		especie = Especie(1, "Mamífero")
		especie.fazer_update("Réptil")
		especie.nome |should| equal_to("Réptil")

	def test_inserir_lista_animais(self):
		especie = Especie(20, "Mamífero")
		animal = Animal(10, "Cachorro", "Macho", especie.nome)   
		animal2 = Animal(30, "Boi", "Macho", especie.nome)      

		especie.inserir_lista_animais(animal)
		especie.inserir_lista_animais(animal2)

		(animal in especie.lista_animais) |should| equal_to(True) 
		(animal2 in especie.lista_animais) |should| equal_to(True)