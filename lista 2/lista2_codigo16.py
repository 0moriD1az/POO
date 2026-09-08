alunos={'gabriel':9.2, 'josé':7, 'zé':6}

for chave, valor in alunos.items():
    
    if valor>=7.0:
      print(f'{chave}, situação: aprovado')

    else:
      print(f'{chave}, situação: reprovado')