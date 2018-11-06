#12 Algoritmo que leia o preço do produto e
# mostre seu novo preço, com 5% de desconto

print("Calcular Preço do produto")
p = float(input("Digite o valor do produto R$: "))

print("Valor do produto {} \nProduto com desconto de 5%: {:.2f}".format(p,p * 0.95))
