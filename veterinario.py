#coding: utf-8
class Veterinario():

	def __init__(self, codVeterinario, nome, crmv):
		self.codVeterinario = codVeterinario
		self.nome = nome
		self.crmv = crmv

	def fazer_update(self, nome_novo, crmv_novo):
		self.nome = nome_novo
		self.crmv = crmv_novo