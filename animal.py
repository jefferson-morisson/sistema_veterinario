#coding: utf-8
from especie import Especie

class Animal():

	def __init__(self, codAnimal, nome, sexo, especie, lista_consultas =[]):
		self.codAnimal = codAnimal
		self.nome = nome
		self.sexo = sexo
		try: 
			especie.__class__ == Especie
			self.especie = especie
		except:
			raise TypeError('especie tem que ser um objeto do tipo Especie')
		self.lista_consultas = []

	def fazer_update(self, nome_novo, especie_nova):
		self.nome = nome_novo
		try: 
			especie_nova.__class__ == Especie
			self.especie = especie_nova
		except:
			raise TypeError('especie tem que ser um objeto do tipo Especie')

	def inserir_lista_consultas(self, consulta):
		self.lista_consultas.append(consulta)