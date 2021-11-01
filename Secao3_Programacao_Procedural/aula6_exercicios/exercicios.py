"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função 2 executada.

2 - Cria uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1 executar duas funções que recebam um número diferente de argumentos.

"""

#1
def ola_mundo():
    return 'Olá mundo'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)


#2
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Kevin')
executando2 = mestre(saudacao, 'Kevin', saudacao='Bom dia')
print(executando)
print(executando2)