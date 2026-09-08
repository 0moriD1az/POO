alunos={'gabriel':{'n1':9, 'n2':10, 'media':9.5}}

nome=list(alunos.keys())[0]
n1=alunos['gabriel']['n1']
n2=alunos['gabriel']['n2']

media=(n1+n2)/2

if media>=7:
    print(f'aluno:{nome}\nnota 1: {n1}\nnota 2: {n2}\nmedia{media}\nsituação: aprovado')
    
else:
    print(f'aluno:{nome}\nnota 1: {n1}\nnota 2: {n2},\nmedia{media}\nsituação: reprovado')
