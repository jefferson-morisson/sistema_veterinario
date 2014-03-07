#coding: utf-8

class Animal():

	def __init__(self, codAnimal, nome, sexo, especie):
		self.codAnimal = codAnimal
		self.nome = nome
		self.sexo = sexo
		try: 
			especie.__class__ == Especie
			self.especie = especie
		except:
			raise TypeError('especie tem que ser um objeto do tipo Especie')