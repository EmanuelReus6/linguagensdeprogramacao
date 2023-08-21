''' Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.'''


lista = ["1","2","3"]

valor = input("digite um possivel elemento: ")

if valor in lista:
    print(f"{valor} esta em {lista.index(valor)} ")



