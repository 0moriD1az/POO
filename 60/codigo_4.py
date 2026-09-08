esc=int(input('Digite 1 para hipotenusa e 2 para cateto: '))

if esc==1:

    c1=float(input('\ndigite o primeiro cateto: '))
    c2=float(input('digite o segundo cateto: '))

    hip=((c1**2)+(c2**2))**0.5

    print(f'A hipotenusa é: {hip}')

elif esc==2:

    c1=float(input('\ndigite o cateto: '))
    hip=float(input('digite a hipotenusa: '))
    
    cat=((hip**2)-(c1**2))**0.5
    
    print(f'O outro cateto é: {cat}')

else:
    print('numero invalido')