"""Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos."""

idade = int(input("Digite a sua idade: "))
tempo = int(input("Digite o tempo de trabalho: "))

if idade >= 65 or tempo >= 30:
    print("pode se aposentar")

elif idade >=60 and tempo >=25:
    print("pode se aposentar")

else:
    print("não pode se aposentar")
