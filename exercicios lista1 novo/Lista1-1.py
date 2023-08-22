"""Faça um script que leia dois números e retorne como resultado a soma deles. Faça um script que leia algo
pelo teclado e mostra na tela o seu tipo de dado."""

#soma
valoru = float(input("digite um valor: "))
valord = float(input("digite um valor: "))

print(f"A soma dos valores {valoru} e {valord} é {valoru + valord}")

#mostra tio dado
dado = input("Digite um dado: ")
print(type(dado))

print("Alphanumerico:",dado.isalnum())
print("Numerico:",dado.isnumeric())
print("Maiusculo:",dado.isupper())
print("Minusculo:",dado.islower())
