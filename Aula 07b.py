n1 = int(input("Digite o Valor: "))
n2 = int(input("Digite outro Valor: "))
s = n1+ n2
m = n1 * n2
d = n1/n2
di = n1//n2
e = n1 ** n2
print("A soma é {}, \nO produto é {}  \nA divisão é {:.3f}".format(s,m,d), end=" ")
print("Divisão por inteiro {} e potência {}".format(di,e))