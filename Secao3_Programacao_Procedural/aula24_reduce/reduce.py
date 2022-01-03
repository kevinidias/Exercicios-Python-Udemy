from functools import reduce


lista = [1,5,6,9,7,9]

soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
print(soma_lista)
