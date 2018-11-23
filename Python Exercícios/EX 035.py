#35 Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o Segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))

if a < b + c  and b < a + c and c < a + b:
    print("Os segmentos acima formam um triangulo")
else:
    print("Não formam um triangulo")

