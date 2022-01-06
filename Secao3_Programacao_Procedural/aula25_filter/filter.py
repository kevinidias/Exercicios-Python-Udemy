lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 15},
    {'nome': 'p3', 'preco': 5},
    {'nome': 'p4', 'preco': 1},
    {'nome': 'p5', 'preco': 16},
    {'nome': 'p6', 'preco': 6},
    {'nome': 'p7', 'preco': 7},
]


nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

def filtra(produto):
    if produto['preco'] > 10:
        return True

#nova_lista_2 = filter(lambda p: p['preco'] > 10, produtos)
nova_lista_2 = filter(filtra, produtos)
for produto in nova_lista_2:
    print(produto)