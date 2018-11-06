#8 Escreva um programa que converta metro em centimetros e milimetros

print("Conversor metros e centimetros")
valor = float (input("Digite um valor: "))
print("O valor {} em cm: {:.0f}cm \nO valor {}"
      " mm: {:.0f}mm".format(valor,valor*100,valor,valor*1000))