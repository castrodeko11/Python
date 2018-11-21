#33 Algoritmo que leia 3 número e mostre qual o maior e qual o menor número
import random

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print("Menor Número: {}\nMaior Número: {}".format(menor,maior))