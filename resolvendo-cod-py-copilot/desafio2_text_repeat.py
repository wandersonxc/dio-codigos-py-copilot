# Entrada de uma string e um número inteiro. Com o retorno da string repetida o número de vezes que foi solicitado.
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

dados_repetidos = (string + " ") * numero

print("A string repetida é:", dados_repetidos)