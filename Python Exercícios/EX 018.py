import math
#18 Seno, cosseno e tangente

#  Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

b = float(input("Digite o ângulo: "))
a = math.radians(b)

print("O seno é {:.2f} \nO coosseno: {:.2f}\nA Tangente é: {:.2f} ".format(math.sin(a),math.cos(a),math.tan(a)))