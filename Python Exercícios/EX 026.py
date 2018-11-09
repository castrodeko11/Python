#26 Algoritmo que leia frase e monstre

n = input("Digite um frase: ")

print("Vezes que aparece letra 'A': {} \nA Posição da "
      "primeira aparição: {}\nPosição da ultima letra a: {}".format(n.count('a'),n.find('a'),n))