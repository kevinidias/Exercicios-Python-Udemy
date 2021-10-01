"""
For / Else em Python
"""

variavel = ['Kevin', 'Joãozim', 'Maria']


start_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        start_j = True

if start_j:
    print('Existe uma palavra que começa com J')
else:
    print('Não existe uma palavra que começa com J')




"""for valor in variavel:
    if valor.startswith('J'): #startswith verifica se a string começa como valor especificado
        print(valor, 'Começa com J')
    else:
        print(valor, 'Não começa com J')"""