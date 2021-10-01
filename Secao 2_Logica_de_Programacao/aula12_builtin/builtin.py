
#https://docs.python.org/3/library/stdtypes.html
#https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py



num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('Error')