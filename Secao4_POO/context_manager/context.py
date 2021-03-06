"""
Criando e usando gerenciadores de contexto.
"""
"""
Exemplo 1:
    class Arquivo:
        def __init__(self, arquivo, modo):
            print('abrindo arquivo')
            self.arquivo = open(arquivo, modo)

        def __enter__(self):
            print('retornando arquivo')
            return self.arquivo

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('fechando arquivo')
            self.arquivo.close()

    with Arquivo('abc.txt', 'w') as arquivo:
        arquivo.write('Alguma coisa')
"""


#Exemplo 2
from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with abrir('abcd.txt', 'w') as arquivo:
    arquivo.write('Novo txt')
    