"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Exemplo: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""

from datetime import time

time = input('Digite a hora atual HH:MM \n')

if int(time[0:2]) <= 11:
    print('Bom dia')
elif int(time[0:2]) <=17:
    print('Boa tarde')
else:
    print('Boa noite')
