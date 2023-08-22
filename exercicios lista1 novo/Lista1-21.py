'''Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''





while True:
    print("a = soma , b = multiplicação , c = maior , d = menor , e = sair")
    op = input("digite uma opção:")

    if op == "a":
        numsoa = float(input("digite o primeiro valor:"))
        numsob = float(input("digite o segundo valor:"))
        print(f"a soma dos valores {numsoa} e {numsob} é {numsoa + numsob}")

    if op == "b":
        nummulta = float(input("digite o primeiro valor:"))
        nummultb = float(input("digite o segundo valor:"))
        print(f"o produto dos valores {nummulta} e {nummultb} é {nummulta * nummultb}")

    if op == "c":
        nummaia = float(input("digite o primeiro valor:"))
        nummaib = float(input("digite o segundo valor:"))
        if nummaia > nummaib:
            print({f"{nummaia} é maior que {nummaib}"})

    if op == "d":
        nummena = float(input("digite o primeiro valor:"))
        nummenb = float(input("digite o segundo valor:"))
        if nummena < nummenb:
            print({f"{nummena} é menor que {nummenb}"})

    if op == "e":
        break
        








