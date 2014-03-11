#coding: utf-8
class Veterinario():

	def __init__(self, codVeterinario, nome, crmv, lista_consultas=[]):
		self.codVeterinario = codVeterinario
		self.nome = nome
		self.crmv = crmv
		self.lista_consultas =[]

	def fazer_update(self, nome_novo, crmv_novo):
		self.nome = nome_novo
		self.crmv = crmv_novo

	def inserir_lista_consultas(self, consulta):
		self.lista_consultas.append(consulta)