# Criar programa que leia a informaçõa e trazer informações do tipo
info = input("Digite algo: ")
print(type(info))
print("É um número: ",info.isnumeric())
print("É alpha: ",info.isalpha())
print("É alphanumperico: ",info.isalnum())
print("É maisculo: ",info.isupper())