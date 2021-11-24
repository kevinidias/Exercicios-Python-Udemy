"""
Listas, tuplas, str são sequencias e são iteraveis.
"""

nome = 'Kevin Dias'
iterador = iter(nome)
gereador = (letra for letra in nome)

print(next(gereador))

print(next(iterador)) #repetindo essa linha temos o nome formado porém caso se repita além dos caracteres dispara um erro que pode ser ajustado com try, except.
print(next(iterador))

for letra in nome: 
    print(letra)