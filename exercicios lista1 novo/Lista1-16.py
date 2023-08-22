"""Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão."""



print("fahrenheit para celsius = 1 / celsius para fahrenheit = 2")
op = int(input("Digite a opção: "))

if (op == 1):
    F = float(input("digite o valor em fahrenheit: "))
    print(f"o valor de {F} F em celsius é {(F-32)/1.8} C")

if (op == 2):
    C = float(input("digite o valor em celsius: "))
    print(f"o valor de {C} C em fahrenheit é {(C*1.8)+32} F")




