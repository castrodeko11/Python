#Aula 10
# Condições no Python  IF and Else
# Analisando condicionais e forma de utilização


tempo = int(input("Quantos anos tem seu carro ? \n"))

if (tempo <=3):
    {

        print("Carro Novo")
   }

else:
    {
        print("Carro Velho")
    }
print("Fim")


print("")
print("Condicional simplificada")
print('Carro Novo' if tempo <=3 else 'Carro Velho')
print("Fim")