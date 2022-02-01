def converte_numero(valor):
    try:
        valor = int(valor)
        return valor    
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
                ...

numero = converte_numero(input('Digite um número: '))

if numero is None:
    print('Isso não é um número')
else:
    print(numero * 5)
    