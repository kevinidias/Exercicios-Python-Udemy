"""
Funções - def em python (Parte 2)
"""

"""def funcao(var): #var = parametro
    
    return var #utilizamos return para retornar um determinado valor

variavel = funcao('Valor que eu quero')"""


def divisao(n1, n2):
    if n2 == 0:
        return
    
    return n1 / n2

divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('Conta inválida.')


