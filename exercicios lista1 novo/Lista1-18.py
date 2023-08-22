"""Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos."""

provaa = float(input("AVL1:digite um valor de 0 a 5: ")) 
provab = float(input("AVL2:digite um valor de 0 a 5: ")) 
provac = float(input("AVL3:digite um valor de 0 a 10: "))  

if provaa > 5 or provaa <0 or provab > 5 or provab <0 or provac > 10 or provac < 0:
    print("valor invalido")
else:
    print(f"media do aluno: {(provaa + provab + provac)/2}")