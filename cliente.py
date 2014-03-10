#coding: utf-8
class Cliente():

	def __init__(self, codCliente, nome, endereco, telefone):
		self.codCliente = codCliente
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone

	def fazer_update(self, nome_novo, endereco_novo, telefone_novo):
		self.nome = nome_novo
		self.endereco = endereco_novo
		self.telefone = telefone_novo