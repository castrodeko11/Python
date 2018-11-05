#11 Criar um algoritmo que leia largura e altura da parede em metro e

print("Calcularia Area")
l = float(input("Digite a largura da parede em metros: "))
a = float(input("Digite altura da parede em metros: "))
area = l*a
print("")
print("Relatório")
print("A area de parede é: {}m2 \nQuantidade de tinta necessária: {} Lts".format(area,area/2))
print("Fim")