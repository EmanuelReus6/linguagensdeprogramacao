"""Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
os itens repetidos.
Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte
a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte."""

x = 0
a = 0
b = 0
c = 0
lista = [1,1,4,3,4]
repetidos = []
filmes = []
jogos = []
livros = []
esporte = []

for i in lista:
    if lista.count(lista[i]) > 1:
        repetidos.append(lista[i])

print("repetidos: " , repetidos)

#lista.count("gabriel")



while x < 2:
    adin = input("digite o item a ser adicionado: ")
    filmes.append(adin)
    x = x + 1 
while a < 2:
    adin = input("digite o item a ser adicionado: ")
    jogos.append(adin)
    a = a + 1
while b < 2:
    adin = input("digite o item a ser adicionado: ")
    livros.append(adin)
    b = b + 1
while c < 2:
    adin = input("digite o item a ser adicionado: ")
    esporte.append(adin)
    c = c  + 1




    #isso é a 34