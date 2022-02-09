from associacao import Escritor, Caneta, MaquinaDeEscrever
from agregacao import CarrinhoDeCompras, Produto

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


