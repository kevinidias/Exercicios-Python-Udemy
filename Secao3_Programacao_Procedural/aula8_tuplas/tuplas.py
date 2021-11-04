"""
Não podemos editar os elementos da tupla.
"""

t1 = (1, 2, 3, 'a', 'Kevin')

print(t1[0]) #acessar valores
print(t1[2:])

for v in t1:
    print(v)


#alterando valor da tupla com lista
t2 = (1, 2, 3, 4)
t2 = list(t2)
t2[1] = 3000
t2 = tuple(t2)

print(t2)