"""
Operadores lógicos
and - duas comparações precisam ser verdadeiras para retornar true
or - qualquer uma que for verdadeira retorna true
not - inverte o valor 
in - existe algo dentro da variável
not in - não existe...
"""

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário:')

usuario_bd = 'Kevin'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')
