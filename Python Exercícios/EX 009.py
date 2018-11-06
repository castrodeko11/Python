#9 Criação de algoritmo para fazer a tabuada

n = int(input("Digite um valor inteiro: "))

c =0
print()
print("Tabuada do {}".format(n))
print("-"*12)
while (c <11):
    print("{} x {:2} = {} ".format(n,c,n*c))
    c +=1
print("-"*12)
print("Fim")