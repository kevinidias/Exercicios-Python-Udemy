produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 15},
    {'nome': 'p3', 'preco': 5},
    {'nome': 'p4', 'preco': 1},
    {'nome': 'p5', 'preco': 16},
    {'nome': 'p6', 'preco': 6},
    {'nome': 'p7', 'preco': 7},
]

lista = [1,5,6,9,7,9]

nova_lista = map(lambda x: x * 2, lista)
nova_lista2 = [x * 2 for x in lista]

print(list(nova_lista))
print(nova_lista2)



precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)




def novo_preco(novo_p):
    novo_p['preco_novo'] = novo_p['preco'] * 2
    return novo_p

novos_precos = map(novo_preco, produtos)

for precos_novos in novos_precos:
    print(precos_novos)