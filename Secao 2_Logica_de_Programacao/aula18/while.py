"""
While em python
Utilizado para realizar ações enquanto uma condição for verdadeira.
Requisitos: Entender condições e operadores.
"""

while True:
    print()

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')

    operador = input('Digite um operador: " +, -, *, / " ')

    sair = input('Deseja sair? [s]Sim [n]Não:')
    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador inválido.')









"""
x = 0 #coluna
while x < 10:
    y = 0 #linha    
    
    while y < 5:
        print(f'{x} {y}')
        y += 1
    x += 1

print('Acabou')
"""



"""
x = 0 
while x <= 100:
    if x == 3:
        x += 1
        #continue # não executa o que estiver abaixo dele.
        break # finaliza o laço quando x == 3
    print(x)
    x += 1
print('Acabou')
"""




"""
while True:
    nome = input("Qual o seu nome?")
    print(f'Olá {nome}!')
"""