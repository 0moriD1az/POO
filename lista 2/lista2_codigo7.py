val=input('digite as notas separadas por espaço ou aperte enter para deixar vazia: ')

if val.strip():
    notas=[float(nota) for nota in val.split()]

try:
    media=sum(notas)/len(notas)
    print(f'a media é: {media}')
except ZeroDivisionError:
    print('impossivel dividir por 0 (lista vazia)')