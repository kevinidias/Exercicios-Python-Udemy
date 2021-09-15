"""
For in em python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'
nova_string = ''

# continue - pula para o próximo laço
# break - brequa nosso laço

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)




"""
for numero in range(0, 10, 2): 
    print(numero)
"""







"""
texto = 'Python'

for letra in texto:
    print(letra)
    """