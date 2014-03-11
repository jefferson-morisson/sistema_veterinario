#coding: utf-8
class Especie():

	def __init__(self, codEspecie, nome, lista_animais = []):
		self.codEspecie = codEspecie
		self.nome = nome
		self.lista_animais = []

	def fazer_update(self, nome_novo):
		self.nome = nome_novo

	def inserir_lista_animais(self, animal):
		self.lista_animais.append(animal)