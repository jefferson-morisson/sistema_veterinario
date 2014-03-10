#coding: utf-8
import unittest
from should_dsl import should
from sistema_veterinario.cliente import Cliente

#Testes com a classe Cliente		
class ClienteTest(unittest.TestCase):
	
	def test_criar_cliente(self):
		cliente = Cliente(1, "João", "Avenida 28 de março", "9 9888-9889")
		cliente.codCliente |should| equal_to(1)
		cliente.nome |should| equal_to("João")
		cliente.endereco |should| equal_to("Avenida 28 de março")
		cliente.telefone |should| equal_to("9 9888-9889")

	def test_fazer_update(self):
		cliente = Cliente(1, "João", "Avenida 28 de março", "9 9888-9889")
		cliente.fazer_update("Gustavo", "Princesa Isabel", "9 9444-9894")
		cliente.codCliente |should| equal_to(1)
		cliente.nome |should| equal_to("Gustavo")
		cliente.endereco |should| equal_to("Princesa Isabel")
		cliente.telefone |should| equal_to("9 9444-9894")