from associacao import Escritor, Caneta, MaquinaDeEscrever
from agregacao import CarrinhoDeCompras, Produto
from composicao import Cliente, Endereco

#instanciando objetos
escritor = Escritor('Kevin')
#print(escritor.nome)
caneta = Caneta('Bic')
#print(caneta.marca)
maquina = MaquinaDeEscrever()
#maquina.escrever()


#associacao

escritor.ferramenta = caneta

escritor.ferramenta.escrever()

print()
#agregacao

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 500)
p3 = Produto('Mouse', 100)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(carrinho.soma_total())

print()
#composicao
cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Maria', 66)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente2.lista_enderecos()