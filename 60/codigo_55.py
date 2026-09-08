def nome_programa():
    '''mostra o nome do sistema'''

    print(f'{'*'*15}SISTEMA DE GERENCIAMENTO ACADÊMICO{'*'*15}\n')

def exibir_menu():
    '''mostra o nome do sistema e as opções disponíveis'''
    
    print(f'{'*'*15}SISTEMA DE GERENCIAMENTO ACADÊMICO{'*'*15}\n')
    print(f'1-cadastrar estudante\n2-listar estudantes\n3-alterar situação\n0-sair\n{'*'*64}\n\n')
   
def cadastrar_estudantes():
    '''opção de cadastro de estudantes(opção 1)'''

    print('opção cadastrar estudante selecionada')

def listar_estudantes():
    '''opção de listagem de estudantes(opção 2)'''

    print('opção listar estudantes selecionada')

def alterar_situacao_estudante():
    '''opção de alterar a situação do estudante(opção 3)'''

    print('opção listar estudantes selecionada')

def finalizar_programa():
    '''opção de finalizar o programa(opção 0)'''

    print('o programa está sendo finalizado')

def opcao_invalida():
    '''função de informar caso a escolha seja equivocada'''

    print(' a opção escolida não existe')


'''main:exibe o menu, recolhe a escolha do teclado e chama a função correspondente'''
exibir_menu()
num=int(input('digite o numero da função desejada: '))

match num:
    case 0:
        finalizar_programa()
    case 1:
        cadastrar_estudantes()
    case 2:
        listar_estudantes()
    case 3:
        alterar_situacao_estudante()
    case _:
        opcao_invalida()

