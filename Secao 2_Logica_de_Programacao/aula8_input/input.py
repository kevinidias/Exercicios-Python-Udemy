"""
Entrada de dados
"""

nome = input("Qual é o seu nome? ")  # input sempre retorna string.
idade = input("Qual é a sua idade? ")

ano_nascimento = 2021 - int(idade)

print()
print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}')

variavel = '5.5'
outra_variavel = (int(float(variavel)))
print(type(outra_variavel))
