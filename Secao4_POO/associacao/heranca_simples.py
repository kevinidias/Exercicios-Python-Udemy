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

class ClienteVip(ClienteH): #sobreposicao 
    def falar(self):
        super().falar() # executa primeiro o metodo falar() que ele achar
        print('outro cliente falando...')


"""
class ClienteVip(ClienteH):
    def __init__(self, nome, idade, sobrenome): usa nome e idade de pessoa.
        super().__init__(self, nome, idade)
        self.sobrenome = sobrenome

"""


class Aluno(Pessoa):
    def estudar(self): #usado apenas em Aluno
        print('estudando...')



#Tira dúvidas
"""
Herança vem de cima para baixo, classes filhos não atingem o pai.
"""

"""
Animal -> respirar
    Logo(Animal) -> respirar / uivar
    Cachorro(Lobo) -> respirar / uivar / latir
    *Somente o cachorro irá latir.
"""


