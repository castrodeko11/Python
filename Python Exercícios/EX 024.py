#24 Algoritmo Que começa ou não com a palavra

n = input("Digite a cidade que nasceu: ").strip()

print("A frase começa com Santo: {}".format(n.upper() in('SANTO')))
print()

print("Analisa mesmo com palavras unidas após eliminar o espaço")
print("A frase começa com Santo: {}".format(n[0:5].upper() in('SANTO')))