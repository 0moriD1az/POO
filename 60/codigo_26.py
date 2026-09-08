idade=float(input('digite a idade: '))

if idade==0 or idade<13:
    print('criança')

elif idade>=13 and idade<=18:
    print('adolescente')

elif idade>18:
    print('adulto')

else:
    print('idade inválida')