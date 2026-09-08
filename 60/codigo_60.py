lista=[]
lmaior=(float(input('digite o limite maior: ')))
lmenor=(float(input('digite o limite menor: ')))

for i in range (0,8):

    lista.append(float(input('digite os milissegundos: ')))

for i in range(len(lista)):
    
    for j in range(0, len(lista) - i - 1):

        if lista[j] > lista[j + 1]:
           
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

final=[x for x in lista if lmenor <= x <= lmaior]

print(final)