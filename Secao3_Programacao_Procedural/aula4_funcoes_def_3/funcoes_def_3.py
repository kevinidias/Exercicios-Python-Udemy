"""
Funções em Python - **args **kwargs
Parte 3
"""
def func(*args, **kwargs): # *args estão empacotados em uma tupla.
    print(args)
    print(kwargs['nome'])

    idade = kwargs.get('idade') #utilizar get caso não tenha certeza que a #chave existe.
    if idade is not None:
        print(idade)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Kevin', idade=30)