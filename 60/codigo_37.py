# números=[int(i) for i in range(1,11)] #forma 1

# for i in range(1,11):  #forma 2
#     números.append(i)

# materias=[]

# for i in range(1,5):
#     nome=input('digite o nome da matéria: ')
#     materias.append(nome)

# print(*materias, sep=", ") #forma 1
# print(", ".join(materias)) #forma 2
# # a terceira forma é for

anos=[]
linhas=int(input('digite quanto pares de dados deseja registrar: '))

for i in range(linhas):
    print(f'====par de dados {i+1}====\n')

    primeiro=input('digite o ano de ingresso: ')
    segundo=input('digite o ano atual: ')

    anos.append([primeiro, segundo])

print(anos)