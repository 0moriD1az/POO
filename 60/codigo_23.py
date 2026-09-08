n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

esc=int(input('Digite 1 para adição (+), 2 para subtração (-), 3 para multiplicação (*) e 4 para divisão (/): '))

match esc:
    case 1:
        print(f'o resultado da adição é: {n1+n2}')
    case 2:
        print(f'o resultado da subtração é: {n1-n2}')
    case 3:
        print(f'o resultado da multiplicação é: {n1*n2}')
    case 4: 
        print(f'o resultado da divisão é: {n1/n2}')
    case _:
        print('valor inválido')