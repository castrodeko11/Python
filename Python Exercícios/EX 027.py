#27 Algoritmo que leia o nome completo e separe primeiro e ultimo nome

n = input("Digite seu nome: ").strip()
nome = n.split()

print("Primeiro nome: {}\nÚltimo nome: {}".format(nome[0],nome[(len(nome)-1)]))
