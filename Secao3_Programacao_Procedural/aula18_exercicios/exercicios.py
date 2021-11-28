"""
Somar uma lista os valores de uma lista de compras usando list comprehensions.
"""

carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 40))
carrinho.append(('Produto3', 30))


total = sum([float(y) for x, y in carrinho])
print(total)