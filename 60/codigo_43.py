notas = [7.5, 8.2, 6.8, 9.1, 5.7, 10.0, 4.3, 7.9, 8.8, 6.5]
contador=0

for i in notas:
    contador+=1
    if i>=7:
        print(f'aluno {contador}: aprovado')

    else:
        print(f'aluno {contador}: reprovado')