"""
Uma classe será dona de objetos de outra classe.
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) #classe Endereco sendo usada para compor um cliente
        #No momento que um cliente é apagado na memória todos os endereços são apagados.

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


