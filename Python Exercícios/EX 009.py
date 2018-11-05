#9 Criação de algoritmo para fazer a tabuada

n = int(input("Digite um valor inteiro: "))

c =0
print()
print("Tabuada")
while (c <11):
    print("{} x {} = {} ".format(n,c,n*c))
    c +=1
print("Fim")