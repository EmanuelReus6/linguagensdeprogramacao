"""Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 ∗ h) − 58
• Mulheres: (62, 1 ∗ h) − 44, 7"""

altura = float(input("Digite a sua altura: "))
print("Feminino = F / Masculino = M")
sexo = input("Escolha a opção correspondente: ")

if sexo == "F":
   print(f'seu peso ideal é {(62.1 * altura) - 44.7}') 

if sexo == "M":
   print(f"seu peso ideal é { (72.7 * altura) - 58}") 


