"""
Formatando valores com modificadores 
:s - Texto  (strings)
:d - Inteiros (int)
:f - Nùmeros de ponto flutuantes (float)
:(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^) (QUANTIDADE)(TIPO -s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao) )

nome = 'Kevin'
sobrenome = 'Dias'
nome_formatado = '{0:0>15} {1:0>15}'.format(nome, sobrenome)
print(nome_formatado)

print(nome.lower()) # tudo minúsculo
print(nome.upper()) # tudo maiúsculo
print(nome.title()) # Primeiras letras maiúsculas