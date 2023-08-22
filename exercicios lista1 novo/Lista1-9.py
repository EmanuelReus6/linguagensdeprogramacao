"""Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
Euros."""

reais = float(input("Digite um valor em reais: "))

print(f"O valor digitado em reais (R${reais}) é equivalente a ${reais/4.98:.3} dolares")
print(f"O valor digitado em reais (R${reais}) é equivalente a €{reais/5.43:.3} euros")