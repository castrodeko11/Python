#13 Algoritmo que leia o salário de um funcioário e monstre seu
# novo salários co 15 % de aumento


print("Algoritmo para aumento salarial")
n = input("Digite o nome do funcionário: ")
v = float(input("Digite o valor do salário: "))

print("O salário atual R$: {} \nAumento "
      "Salarial de 15%: {:.2f}".format(v,v*1.15))