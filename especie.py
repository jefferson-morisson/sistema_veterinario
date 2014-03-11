#coding: utf-8
class Especie():

	def __init__(self, codEspecie, nome):
		self.codEspecie = codEspecie
		self.nome = nome


	def fazer_update(self, nome_novo):
		self.nome = nome_novo