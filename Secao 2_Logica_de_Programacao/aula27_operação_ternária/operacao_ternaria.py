"""
Operador ternário em Python
"""

logged_user = False
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

idade = 17
e_maior = (idade >=18)
msgi = 'Pode acessar' if e_maior else 'Não pode acessar.'
print(msgi)

"""
logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'
"""