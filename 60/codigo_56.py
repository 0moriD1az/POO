hP=float(input('digite a carga horária para programação: '))
hB=float(input('digite a carga horária para banco de dados: '))
hR=float(input('digite a carga horária para redes de computadores:'))

if hP<0 or hB<0 or hR<0:
    print('valores inválidos')

else:
    total=hP+hB+hR

    print(f'a carga horária total é de {total} horas')