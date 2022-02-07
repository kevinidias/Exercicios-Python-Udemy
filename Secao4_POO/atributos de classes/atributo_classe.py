class A:
    vc = 123 # atributo de classe que está disponivel para todas as instancias.


A.vc = 'alterado' #altera valor do atributo da classe de todas as instancias.

a1 = A()  #instancia
a2 = A()
print(a1.vc)
print(a2.vc)


