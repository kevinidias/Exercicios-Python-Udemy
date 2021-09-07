"""
Operadores relacionais.
 == > >= <= !=
"""

nome = input("Qual o seu nome?")
idade = input("Qual sua idade?")

# Limite para pegar emprestimo
# Entre 20 e 30 anos
idade_menor = 20
idade_maior = 30

if int(idade) >= idade_menor and int(idade) <= idade_maior:
    print("Pode fazer o emprestimo")
else:
    print("Não pode fazer o emprestimo")


