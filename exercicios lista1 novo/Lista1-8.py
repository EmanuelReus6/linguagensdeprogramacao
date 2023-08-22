"""Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²."""

larg = float(input("Digite a largura da parede: "))
altu = float(input("Digite a altura da parede: "))

print(f"A area da parede é {larg*altu} m²")

print(f"A quantidade de tinta necessaria é {(larg*altu)/2} l")

