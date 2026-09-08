lista=[]
contador=0

while contador<10:
    n=int(input('digite o número inteiro divisível por 6: '))

    if n % 6 != 0:
        print('númerp inválido!')
        continue
    else:
        lista.append(n)

        print(f'\nnúmero preenchido na posição {contador+1}' , end=',')
        print(f'números na lista: {lista}, total de números: {contador+1}\n')
        contador+=1

else:
    print(f'lista completa! Lista: {lista}')