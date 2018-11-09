n = str(input("Digite seu nome: ")).strip()
print("Nome em maiusculo: {} ".format(n.upper()))
print("Nome em minusculo: {} ".format(n.lower()))
print("Nome QTD Sem considerar espaços: {}".format(len(n) - n.count(' ')))

n1 = n.split()
print("Primeiro Nome: {} QTD caracteres: {}".format(n1[0],len(n1[0])))

# Localizar o primeiro espaço tras a qtd de caracteres print(n.find(' '))
