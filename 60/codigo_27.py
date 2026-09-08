dados={'nome':'Fesor', 'senha':'D0m1No' }

nomeinfo=input('digite o nome de usuário (maiúsculas importam):  ')
senhainfo=input('digite a senha (maiúsculas importam): ')

if nomeinfo==dados['nome'] and senhainfo==dados['senha']:
    print('acesso liberado!')

else:
    print('informações incorretas, você é meu inimigo')