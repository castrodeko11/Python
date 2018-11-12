#26 Algoritmo que leia frase e monstre

n = input("Digite um frase: ").upper().strip()

print("Vezes que aparece letra 'A': {} \nA Posição da "
      "primeira aparição: {}\nPosição da ultima letra "
      "a: {}".format(n.count('A'),n.find('A')+1,n.rfind("A")+1))
