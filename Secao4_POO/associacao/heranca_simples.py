"""
Herança funciona de cima para baixo.

"""


class Pessoa:
    def __init__(self, nome, idade): #atributos usados em classes que herdam 
        self.nome = nome
        self.idade = idade

    def falar(self): # método usado em classes que herdam pessoa
        print('falando')


class ClienteH(Pessoa):
    def comprar(self): #usado apenas em ClienteH
        print('comprando...')


class Aluno(Pessoa):
    def estudar(self): #usado apenas em Aluno
        print('estudando...')
