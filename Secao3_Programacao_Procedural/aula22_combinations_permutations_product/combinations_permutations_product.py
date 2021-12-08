"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['luiz', 'kevin', 'andré', 'maria', 'joana', 'fabiana']

for grupo in permutations(pessoas, 2): #repeat=2 para product
    print(grupo)