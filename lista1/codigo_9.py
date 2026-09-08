a=float(input('digite o primeiro número: '))
b=float(input('digite o segundo número: '))
c=float(input('digite o terceiro número: '))

if a+b<=c or a+c<=b or b+c<=a:

    print('os valores informados não podem formar um triângulo')
    exit()

elif a==b and b==c:
    print('o triangulo é equilátero')

elif a!=b and b!=c:
    print('o triangulo é escaleno')

else:
    print('o triangulo é isósceles')

