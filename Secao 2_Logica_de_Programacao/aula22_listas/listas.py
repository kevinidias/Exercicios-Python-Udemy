"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, + 
min, max
range
contém vários valores dentro de colchetes []
str, bool, int, float
"""

#palavra secreta
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUL, a letra {letra} existe na palavra secreta')
    else:
        print(f'AAF a letra {letra} NÃO EXISTE na palavra secreta')
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Você ganhou!!! A palavra era "{secreto_temporario}"')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()

"""
l1 = list(range(1,10))
l2 = list(range(10,21))

soma = 0 
for valor in l2:
    soma = soma + valor
print(soma)
"""


"""

lista = ['A', 'B', 'C' , 'D', 'E']

#acessar valor A
print(lista[0])

#fatiamento
print(lista[0:3])


#inserir valor ao final da lista
l2.append('b')

#inserir valor em uma posição específica da lista
l2.insert(0, 'maçã') #começo da lista

#remover ultimo elemento da lista
l2.pop()

#remover fatia de elementos
del(l2[0:2])

#valor máximo da lista
print(max(l2))
print(min(l2))

#l1.extend(l2)
#l3 = l1 + l2 

print(l1)
print(l2)
#print(l3)
"""