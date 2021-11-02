# passar uma função para outra função 


lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 10],
    ['P4', 50],
    ['P5', 7],
]

#ordena a lista sem precisar criar uma função pra isso.
lista.sort(key=lambda item: item[1])
print(sorted(lista, key=lambda i: i[0]))
print(lista)

"""a = lambda x, y: x * y
print(a(2,2))
"""