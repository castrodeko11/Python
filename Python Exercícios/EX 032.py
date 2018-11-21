#032 Algoritmo para verificar se o ano é bissexto

import datetime
n = int(input("Digite se o ano: "))

if (n % 4 == 0 and n % 100 != 0 or n % 400 ==0):
    {
        print("O ano {} é Bissexto".format(n))
    }

else:
    {
        print("O ano {} não é Bissexto".format(n))
    }



print(datetime.date.today().year)