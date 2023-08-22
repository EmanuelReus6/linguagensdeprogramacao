"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

while True:
    usu = input("digite o nome do usuario: ")
    sen = input("digite uma senha: ")

    if sen == usu:
        print("Senha tem que ser diferente de usuario")

    else:
        break