#28 Algoritmo que faça computador pensar em um número inteiro de (0,5)
import random
import time
list = [0,1,2,3,4,5]
s = random.choice(list)
n = int (input("Digite um número "))

if (s == n):
    {

        print("Número Sorteado: {} \nVocê Acertou".format(s))

    }
else:
    print("Número Sorteado: {} \nVocê Errou".format(s))



# Outra forma
print()
print("Outra forma ")
computador = random.randint(0,5) # Faz o computador "Pensar"
print("-=-"*20)
print("Vou pensar em um número entre 0...5. Tente Descobir...")
print("-=-"*20)
player = int (input("Digite um número que pensei ")) # Jogador tentnado adivinhar
print("Processando...")
time.sleep(3)

if (computador == player):
    {

        print("Número Sorteado: {} \nVocê Acertou".format(computador))

    }
else:
    print("Número Sorteado: {} \nVocê Errou".format(computador))

