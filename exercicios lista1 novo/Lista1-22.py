'''Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada.'''
valor = 0
quant = 0
soma = 0
while True:
    valor = int(input("digite um valor: "))

    if valor == 1000:
        break

    else:
        quant += 1
        soma += valor

print(f"{quant} numeros foram digitados, sua soma é {soma}")
