"""
_ atributo privado, mas conseguimos acessar. (_nomeatributo)
__ atributo fortemente privado (_NOMEDACLASSE__nomeatributo)

Atributo criado para ser acessado somente dentro de uma determinada classe.
"""

class BaseDeDados():
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Kevin')
bd.inserir_cliente(2, 'Kevin2')
bd.inserir_cliente(3, 'Kevin3')
bd.apaga_cliente(2)
bd.lista_clientes()