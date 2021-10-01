"""
Split, Join, Enumerate em Python
* Split - Dividir uma string baseado no valor que eu quiser #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista #list
"""


lista = [
    [1,2],
    [3,4],
    [5,6]
]

for v in lista:
        print(v[0], v[1])



string = "O Brasil é penta."
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)





"""string = "O Brasil é penta."
lista = string.split(' ')
string2 = ','.join(lista)
print(string2)"""





"""string = "O Brasil é o país do futebol, o Brasil é penta."

lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)"""

