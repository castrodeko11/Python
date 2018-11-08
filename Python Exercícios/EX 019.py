#19 Exercício de sorteio

# Criar sorteio de nomes

import random

n1 = input("Digite o primeiro nome: ")
n2 = input("Digite o primeiro nome: ")
n3 = input("Digite o primeiro nome: ")
n4 = input("Digite o primeiro nome: ")

lista = [n1,n2,n3,n4]


print("O nome sorteado é: {}".format(random.choice(lista)))



