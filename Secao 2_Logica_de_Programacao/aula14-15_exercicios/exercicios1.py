"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""


numinteiro = input('Digite um número ')


if not numinteiro.isdigit():
    print('Usuário não digitou um número')
elif int(numinteiro) % 2 == 0:
    print('Número é par')
else:
    print('Número é ímpar')


