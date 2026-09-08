ini=float(input('digite o valor inicial: '))
j=float(input('digite a taxa de juros (porcentagem ao mes): '))
tem=float(input('digite tempo (em meses): '))

conv_juros=j/100

juros=ini*conv_juros*tem
final=ini+juros

print(f'os juros somam: {juros} e o valor final é: {final}')