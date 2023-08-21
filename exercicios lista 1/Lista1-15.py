"""Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
tela dizendo se está “quente”, “frio” ou “agradável”."""

temp = int(input("Digite uma temperatura: "))

if (temp < 15):
    print("Frio")

if (temp >= 15) and (temp < 22):
    print("Agradavel")

if (temp > 22):
    print("Quente")
