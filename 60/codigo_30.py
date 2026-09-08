nota = float(input("Digite a nota (0 a 10): "))


if nota>=7 and nota<=10:
    print('aprovado')
elif nota>=5 and nota<7:
    print('recuperação')
elif nota<5 and nota>=0:
    print('reprovado')

else:
    print('nota inválida')
