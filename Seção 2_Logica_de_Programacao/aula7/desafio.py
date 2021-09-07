"""
* Criar variáveis para nome, idade, altura e peso de uma pessoa,
* Criar variável com o ano atual
* Obter o ano de nascimento da pessoa (baseado na idade atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings {}
"""

nome = 'Kevin'
idade = 25
altura = 1.58
peso = 68
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome}, tem {idade} anos de idade com {altura} de altura, pesa {peso} '
      f'kg nascido em {nascimento}, com o imc de {imc:.2f}')

