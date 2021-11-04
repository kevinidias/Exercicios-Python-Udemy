"""
Dicionários
Chave e valor
Podemos utilizar valores imutáveis.
Quando tentamos acessar chaves que não existe temos um erro.
"""

d1 = {'chave1': 'valor da chave', 'chave3': 'chave3'}
d1['nova_chave'] = 'Valor da nova chave'
del d1['chave1']
print('nova_chave' in d1)
print('nova_chave' in d1.keys())
print('nova_chave' in d1.values())
print(d1)

for k in d1:
    print(k)

d2 = dict(chave1='valor da chave')
print(d2)

