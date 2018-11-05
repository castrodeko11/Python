#7 Programa que leia as duas notas de um aluno e calcule as médias

print("Média do Aluno")
n = input("Digite seu nome: ")
n1 = float(input("Digite a 1ª Nota: "))
n2 = float(input("Digite a 2ª Nota: "))

m= (n1+n2)/2
print("")
print("Aluno: {} \nMédia: {}".format(n,m))