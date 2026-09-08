tempo=[float(x) for x in input('digite os quatro tempos separados por espaço (em milissegundos): ').split()[:4]]

atual=tempo[0]

for n in tempo:
    if atual>n:
        atual=n

print(f'o menor tempo é de {atual}')
        