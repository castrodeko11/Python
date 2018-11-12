#Prática Aula 10
print("Informações do usuário ")
n = str(input("Qual seu nome? \n"))
print("Bom dia {}".format(n))
if n == "André":
    {
        print("Nome Perfeito")
    }
else:{
    print("Nome normal")
}
print("")

print("Relatório de notas")
n1 = float(input("Digite 1ª Nota: "))
n2 = float(input("Digite 1ª Nota: "))
m = (n1+n2)/2
print("A sua média é {}".format(m))

if (m >= 6.0):
    print("Sua média foi boa! Parabéns")
else:
    print("Sua média foi Ruim! Estude Mais")

print("Fim do Relatório")

