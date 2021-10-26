"""
1- Crie uma função que exibe uma saudação com os parâmetros saudação e nome.

2- Cria uma função que recebe 3 números como parêmetros e exiba a soma entre eles.

3- Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo. 

4- Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""


#1
def saudacao(saudacao='Bem-vindo', nome='Kevin'):
    return f'{saudacao} {nome}'

saud = saudacao()
print(saud)


#2
def adicao(n1, n2, n3):
    n = n1 + n2 + n3
    return n

soma = adicao(2, 3, 4)
print(soma)


#3
def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)

ap = aumento_percentual(50, 10)
print(ap)

#4
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n

print(fb(7))
print(fb(10))
print(fb(15))
print(fb(22))