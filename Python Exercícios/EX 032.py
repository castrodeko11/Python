#032 Algoritmo para verificar se o ano é bissexto

n = int(input("Digite se o ano: "))

if (n % 4 == 0):
    {
        print("O ano {} é Bissexto".format(n))
    }
else:
    {
        print("O ano {} não é Bissexto".format(n))
    }
