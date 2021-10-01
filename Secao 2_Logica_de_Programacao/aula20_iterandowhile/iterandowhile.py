
frase = 'o rato roeu a roupa do rei de roma' #strings contém items, que contém valores iteráveis 
tamanho_frase = len(frase)

contador = 0
nova_string = ''

input_usuario = input('Qual letra deseja colocar maiúscula? ')


#iteração, percorrendo elementos de uma string
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1


print(nova_string)