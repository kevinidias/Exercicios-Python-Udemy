from itertools import zip_longest


"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

cidades = ['Rio de janeiro', 'São Paulo', 'Salvador', 'Joinville']

estados = ['RJ', 'SP', 'BA']

cidades_estados = zip(estados, cidades)

cidades_estados_longest = zip_longest(estados, cidades, fillvalue='Estado')

print(dict(cidades_estados))
print(dict(cidades_estados_longest))

"""for valor in cidades_estados:
    print(valor)
"""
