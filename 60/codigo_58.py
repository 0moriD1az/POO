c1=input('curso 1: ')
c2=input('curso 2: ')

cm='a'

if c2>c1:
    cm='o curso com mais matrículas é o c2'
    print(f'o curso com mais matrículas é o c2')

elif c1>c2:
    cm='o curso com mais matrículas é o c1'
    print(f'o curso com mais matrículas é o c1')

else:
    print('ambos estão empatados')

with open(
    'maior_matricula.txt',
    'a',
    encoding='utf-8') as arquivo:

    arquivo.write(cm)