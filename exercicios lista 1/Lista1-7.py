"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
de aumento."""

prod = float(input("Digite o valor do produto: "))

print(f"valor do produto com 5% de desconto: {prod - ((prod*5)/100)}")
print(f"valor do produto com 15% de aumento: {prod + ((prod*15)/100)}")

