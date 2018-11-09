# Aula 09
# As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(), transformações com replace(), upper(),
# lower(), capitalize(),
# title(), strip(), junção com join().

frase = "Curso em Video Python"
print("Fatiamento")

# Print caracter específico
print("Caracter Específico")
print(frase[9])
print()

print("Intervalo Específico")
# Print intervalo
print(frase[9:14])
print()

print("Intervalo Específico e pulando 2 casas")
# Print intervalo
print(frase[9:21:2])


print("Intervalo Específico e pulando 3 casas")
# Print intervalo e não inserindo valor final, o pyhton compreende e irá ler informação
print(frase[9::3])
print()


print("Usando count para verificar alguma repetição de caracteres")
print(frase.count('o'))
print()

print("Usando count para verificar alguma repetição de caracteres e intervalo de fatiamento")
print(frase.count('o',0,13))
print()

print("Usando Find localizar algo e o inicio do indice")
print(frase.find('deo'))
print()

print("Usando In para analisar True or False")
print('Curso' in frase)
print()

print("Usando Replace")
print(frase.replace('Python','Android'))
print()

print("Usando upper Maiusculo")
print(frase.upper())
print()

print("Usando lower Minusculo")
print(frase.lower())
print()

print("Usando capitalize Apenas primeiro caracter Maiusculo")
print(frase.capitalize())
print()

print("Usando Title Transformar todas primeiras letrar em Maisculo das pavras")
print(frase.title())
print()

print("-"*5 + "2 Etapa " + "-"*5)
frase1 ='   Aprenda Python  '
print("Usando strip remoção de espaços desnecessário")
print(frase1.strip())
print(frase1)
print()
print("Usando rstrip remoção de espaços desnecessário da direita")
print(frase1.rstrip())
print(frase1)
print()
print("Usando lstrip remoção de espaços desnecessário da esquerda")
print(frase1.lstrip())
print(frase1)
print()
print("Usando split separar blocos por espaços novos indices")
print(frase.split())
print(frase)
print()

print("Usando join para juntar indice para todos")
#'-'.join(frase) ou ""
frase1.split()
print(''.join(frase1))
print(frase1)
print()







