"""Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores"""

valor = 0
quant = 0
soma = 0
op = "s"
maior = 0
menor = 999999999999999999999999999999999999999999999999999
while op != "n":
    valor = int(input("digite um valor: "))

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor


    quant += 1
    soma += valor

    op = input("deseja continuar?(s/n): ")

print(f"maior valor: {maior} , menor valor: {menor} , media dos valores: {soma / quant}")