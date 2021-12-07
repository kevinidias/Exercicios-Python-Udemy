"""
count - Itertools

"""

from itertools import count

contador = count() # parametros start, step,

for valor in contador:
    print(valor)

    if valor >= 10:
        break