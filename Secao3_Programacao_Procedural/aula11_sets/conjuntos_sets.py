"""
Conjuntos
add (adicional), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elemtnso apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

s1 = {1,2,3,4,5,6, 7, 7} # só recebem valores e suportam imutáveis.
# Não respeitam ordem
# Não aceitam elementos duplicados

s1.add(1)
s1.update('a')
s1.discard(6)

print(s1)