from associacao import Escritor, Caneta, MaquinaDeEscrever


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