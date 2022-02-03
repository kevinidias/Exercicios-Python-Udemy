from pessoa import Pessoa

p1 = Pessoa('Kevin', 26, 'lasanha') #instanciando objeto p1 a partir da classe Pessoa.
p1.comer('maçã')
p1.falar('PO')
p1.parar_comer()
p1.falar('POO')
p1.comer('maçã')
p1.parar_falar()
p1.falar('POO')



p2 = Pessoa('Kevin2', 32, 'lasanha')
p2.parar_comer()
p2.falar('Filmes')

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())



p1.nome = 'Kevin' # variaveis de instancia são chamados de atributos da classe.
p2.nome = 'Kevin2' # nome é um atributo da classe Pessoa.


