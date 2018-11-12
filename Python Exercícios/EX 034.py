#34 Algortimo que pergunte salário do funcionário e calcule o aumento
# SalárisSuperiores a R$ 1.250 aumento de 10%
#Inferioes ou iguais a o aumento é de 15%


v = float(input("Digite seu salário: "))

if (v > 1250):
    {
        print("O salário atual é R$ {}\nAumento Salarial de 10% R$: {:.2f} ".format(v,v*1.10))
    }
else:
    print("O salário atual é R$ {}\nAumento Salarial de 15% R$: {:.2f} ".format(v, v * 1.15))