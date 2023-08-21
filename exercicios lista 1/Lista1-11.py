"""Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
ao final mostrar seu nome e salário final calculado."""

nome = input("Nome do funcionário: ")

hora = int(input("Digite o numero de horas trabalhadas: "))

valho = float(input("valor da hora trabalhada: "))

print(f"valor do salario bruto de {nome}: R${hora*valho}")

print(f"valor do salario de {nome} descontado (INSS): R${(hora*valho) - (((hora*valho)*2)/100)}")