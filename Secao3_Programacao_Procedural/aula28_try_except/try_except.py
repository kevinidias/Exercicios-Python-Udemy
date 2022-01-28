"""
Exceções são erros que ocorrem no código.
Simular ao if else.
"""

try:
    print(a)
except NameError as erro: #IndexError, Exception, KeyError...
    print('Erro', erro)


