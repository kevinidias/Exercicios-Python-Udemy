lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x.upper(): y*2 for x, y in lista }
d2 = dict(lista) #fazemos a mesma coisa, porém com o comprehensions podemos fazer alterações.
print(d1)
print(d2)