#23 Algoritmo para mostrar cada um dos números separedos

num = int(input("Digite um número: "))
#
# n = str(num)
#
# print("Analisando o número {} \nUnidade: {}\nDezena: {}"
#       "\nCentena: {}\nMilhar: {}".format(num,n[3],n[2],n[1],n[0]))


u = num //1 % 10
d = num //10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisando o número {} \nUnidade: {}\nDezena: {}"
      "\nCentena: {}\nMilhar: {}".format(num,u,d,c,m))




