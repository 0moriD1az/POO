nome=input('digite seu nome: ')
nasc=int(input('digite o ano do seu nascimento: '))

idade=2026-nasc

if idade>=18:

    print(f'{nome}, você tem {idade} anos, a sua entrada é permitida')

else:
     print(f'{nome}, você tem {idade} anos, a sua entrada é negada')
