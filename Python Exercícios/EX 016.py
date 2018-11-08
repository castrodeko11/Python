import math
#16 Quebrando um núemro
# Criação de um algoritmo para deixar o numero inteiro

''' n = float(input("Digite um número: "))
# print("O número digitado {} e o número inteiro {}".format(n,int(n)))'''


#Usando a biblioteca math para quebrar o número em inteiro
n = float(input("Digite um número: "))
print("O número digitado {} e o número inteiro {}".format(n,math.trunc(n)))

