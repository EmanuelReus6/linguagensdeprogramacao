"""Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele"""

dado = input("digite um dado: ")

print("Alphanumerico:",dado.isalnum())
print("Numerico:",dado.isnumeric())
print("Maiusculo:",dado.isupper())
print("Minusculo:",dado.islower())