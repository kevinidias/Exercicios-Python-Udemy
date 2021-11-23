"""
Geradores, iteradores e iteraveis.
"""

import sys
import time

lista = list(range(10))

print(sys.getsizeof(lista))

def gera():
    for n in range(3):
        yield n
        time.sleep(0.1)
    

g = gera()
print (g)
for v in g: 
    print(v)

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))


print(sys.getsizeof(l1))
print(sys.getsizeof(l2))