#coding: utf-8
from veterinario import Veterinario
from animal import Animal

class Consulta():

	def __init__(self, codConsulta, data, veterinario, animal, resumoConsulta):
		self.codConsulta = codConsulta
		self.data = data
		
		#Exceção para saber se o veterinário é um objeto
		try: 
			veterinario.__class__ == Veterinario
			self.veterinario = veterinario
		except:
			raise TypeError('veterinario tem que ser um objeto do tipo Veterinario')

		#Exceção para saber se o animal é um objeto
		try:
			animal.__class__ == Animal
			self.animal = animal
		except:
			raise TypeError('animal tem que ser um objeto do tipo Animal')

		self.resumoConsulta = resumoConsulta