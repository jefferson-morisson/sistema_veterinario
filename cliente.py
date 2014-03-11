#coding: utf-8
class Cliente():

	def __init__(self, codCliente, nome, endereco, telefone, lista_animais =[]):
		self.codCliente = codCliente
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone
		self.lista_animais =[]

	def fazer_update(self, nome_novo, endereco_novo, telefone_novo):
		self.nome = nome_novo
		self.endereco = endereco_novo
		self.telefone = telefone_novo

	def inserir_lista_animais(self, animal):
		self.lista_animais.append(animal)