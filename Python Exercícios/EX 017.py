import math
#17 Hipotenusa

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
#mostre o comprimento da hipotenusa.

co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
# print("o Valor do Cateto {}\nO Valor do Cateto adjacente {}\nA "
#       "hipoteusa é {:.2f}".format(co,ca,(co**2+ca**2)**(1/2)))


print("o Valor do Cateto {}\nO Valor do Cateto adjacente {}\nA "
      "hipoteusa é {:.2f}".format(co,ca,math.hypot(co,ca)))

