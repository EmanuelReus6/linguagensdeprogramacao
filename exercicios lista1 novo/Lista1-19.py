"""Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção: """
"""a. Soma de 2 n´umeros.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero)."""


print("escolha uma operação: a = soma , b = diferença , c = multiplicação , d = divisão")

op = input("digite a opção: ")

if op == "a":
    numsoa = float(input("digite o primeiro valor:"))
    numsob = float(input("digite o segundo valor:"))
    print(f"a soma dos valores {numsoa} e {numsob} é {numsoa + numsob}")

if op == "b":
    numdifa = float(input("digite o primeiro valor:"))
    numdifb = float(input("digite o segundo valor:"))
    print(f"a diferença dos valores {numdifa} e {numdifb} é {numdifa - numdifb}")

if op == "c":
    nummulta = float(input("digite o primeiro valor:"))
    nummultb = float(input("digite o segundo valor:"))
    print(f"o produto dos valores {nummulta} e {nummultb} é {nummulta * nummultb}")

if op == "d":
    numdiva = float(input("digite o primeiro valor:"))
    numdivb = float(input("digite o segundo valor:"))
    print(f"a divisão dos valores {numdiva} por {numdivb} é {numdiva / numdivb}")


