#15 Aluguel de carros
# Criação de um algoritmo para validação do percurso do carro e os gastos

print("Aluguel de Carro")
print("-"*12)

km = float(input("Digite a quantidade de KM percorridos: "))
d = int(input("Digite a qtd de dias que foi alugado: "))

print("Orçamento Referente ao Aluguel do Carro")
print("-"*12)
print("A QTD de KM {}\nA QTD de dias {}\nCusto do"
      " Aluguel R$: {:.2f}".format(km, d , d*60 + km * 0.15))

