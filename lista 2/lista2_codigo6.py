num=int(input('digite o número para a tabuada (1 a 10): '))

if num>0 and num<11:
    for i in range(1,11):

        print(f'{num} X {i} = {num*i} ')

else:
    print('número inválido')