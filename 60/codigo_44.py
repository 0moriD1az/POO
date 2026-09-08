notas=[]
contador=1

n=float(input(f'digite a {contador} nota: '))
notas.append(n)

maior=notas[0]
menor=notas[0]

for i in range (1,5):

    contador+=1

    n=float(input(f'digite a {contador} nota: '))
    notas.append(n)

    if n>maior:
        maior=n

    if n<menor:
        menor=n

media=sum(notas)/len(notas)
print(f'lista: {notas}')
print(f'média: {media}, maior: {maior}, menor: {menor}')