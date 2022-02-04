from hamcrest import any_of


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self): #método de instancia
        print(self.ano_atual - self.idade)

    @classmethod #método da classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

#p1 = Pessoa('Kevin', 26)
p1_por_ano = Pessoa.por_ano_nascimento('Kevin2', 1996)
print(p1_por_ano)
print(p1_por_ano.nome, p1_por_ano.idade)
p1_por_ano.get_ano_nascimento()