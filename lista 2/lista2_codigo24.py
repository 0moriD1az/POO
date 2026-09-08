lista=['ana', 'roger', 'fernando', 'duda', 'iuri']

contador=0

for n in lista:
    print(f'olá, {n}. convido-o para o jantar')
print('\n\n')
lista[0]='joana'

for n in lista:
    print(f'olá, {n}. convido-o para o jantar')

lista.insert(0, 'sanji')
lista.insert(3,'zoro')
lista.append('tereza')

print(lista)

while contador<6:

    print(f'prezado(a) {lista[0]}, vai dar pra vir não, mals')
    contador+=1

    del lista[0]

for n in lista:
    print(f'{n} ainda está convidado(a)')

lista.clear()

print(lista)

