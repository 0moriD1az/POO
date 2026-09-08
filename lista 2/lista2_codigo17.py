agenda={'joana':4000,'joao':3000,'maria': 2000}

nome=input('digite um nome: ')
n=0

for chave, valor in agenda.items():

    if nome == chave:
        print(f'nome:{chave}, valor: {valor}')

    else:
        n+=1

if n==len(agenda):
    print('contato não encontrado')

