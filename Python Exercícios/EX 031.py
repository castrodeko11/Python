#031 Algoritmo que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem
# Cobrando R$ 0,50 por KM para viagens de até 200 KM
# R$ 0,45 para viagens mais longas


n = float(input("Digite a distância da viagem: "))

if (n <=200):
    {
        print("Distância da viagem: {} KM\nValor da viagem R$: {:.2f}".format(n,n*0.50))

    }
else:
    {

        print("Distância da viagem: {} KM\nValor da viagem R$: {:.2f}".format(n, n * 0.45))
    }



