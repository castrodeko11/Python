#29 Algoritmo que leia velocidade de um carro

v = float(input("Digite a velocidade do carro em KM/h: "))

if (v > 80):
    {
        print("Relatório do Carro"),
        print("Sua velocidade é: {} KM/h \nSuperior a velocidade "
              "permitida de 80KM/h".format(v)),
        print("\nPara cada KM/h supeiro velocidade permitida "
              "é aplicado R$ 7,00 de multa\nKM/h "
              "ultrapassados: {:.0f} KM/h \nValor da"
              " Multa R$: {:.2f}".format(v-80,(v-80)*7))
    }

