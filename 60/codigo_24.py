valores=[0,0,0,-163, 1900]
soma=0
cont=0

for n in valores:

    if n > 1000 or n <= 0:
        continue

    soma+=n
    cont+=1

if cont==0:
    print('nenhum valor dentro dos parâmetros')
    exit()

print(f'a média é: {soma/cont}')