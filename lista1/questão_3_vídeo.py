# Lista para armazenar os equipamentos. Cada item será um dicionário.
equipamentos = []

def cadastrar_equipamento():
    nome = input("Digite o nome do equipamento: ").strip()
    try:
        custo = float(input("Digite o custo estimado do reparo (R$): "))
        equipamentos.append({"nome": nome, "custo": custo})
        print(f"Equipamento '{nome}' cadastrado com sucesso!\n")
    except ValueError:
        print("Erro: Digite um valor numérico válido para o custo.\n")

def listar_equipamentos():
    if not equipamentos:
        print("Nenhum equipamento cadastrado.\n")
        return
    
    print("\n--- LISTA DE EQUIPAMENTOS ---")
    for i, eq in enumerate(equipamentos):
        print(f"ID: {i} | Nome: {eq['nome']} | Custo do Reparo: R$ {eq['custo']:.2f}")
    print("------------------------------\n")

def atualizar_equipamento():
    listar_equipamentos()
    if not equipamentos:
        return
    
    try:
        idx = int(input("Digite o ID do equipamento que deseja atualizar: "))
        if 0 <= idx < len(equipamentos):
            novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ").strip()
            novo_custo_str = input("Digite o novo custo (ou pressione Enter para manter o atual): ").strip()
            
            if novo_nome:
                equipamentos[idx]["nome"] = novo_nome
            if novo_custo_str:
                equipamentos[idx]["custo"] = float(novo_custo_str)
                
            print("Dados atualizados com sucesso!\n")
        else:
            print("Erro: ID inválido.\n")
    except ValueError:
        print("Erro: Entrada inválida.\n")

def excluir_equipamento():
    listar_equipamentos()
    if not equipamentos:
        return
    
    try:
        idx = int(input("Digite o ID do equipamento que deseja excluir: "))
        if 0 <= idx < len(equipamentos):
            removido = equipamentos.pop(idx)
            print(f"Equipamento '{removido['nome']}' removido com sucesso!\n")
        else:
            print("Erro: ID inválido.\n")
    except ValueError:
        print("Erro: Digite um número inteiro válido para o ID.\n")

def maior_custo():
    if not equipamentos:
        print("Nenhum equipamento cadastrado para comparar.\n")
        return
    
    # Encontra o elemento com o maior valor na chave 'custo'
    maior = max(equipamentos, key=lambda x: x["custo"])
    print(f"\n--- EQUIPAMENTO COM MAIOR CUSTO DE REPARO ---")
    print(f"Nome: {maior['nome']} | Custo: R$ {maior['custo']:.2f}\n")

def menu():
    while True:
        print("=== SISTEMA DE MANUTENÇÃO - TI ===")
        print("1. Cadastrar equipamento (Create)")
        print("2. Listar equipamentos (Read)")
        print("3. Atualizar equipamento (Update)")
        print("4. Excluir equipamento (Delete)")
        print("5. Exibir equipamento com maior custo")
        print("6. Sair")
        
        opcao = input("Escolha uma opção (1-6): ").strip()
        print()
        
        if opcao == "1":
            cadastrar_equipamento()
        elif opcao == "2":
            listar_equipamentos()
        elif opcao == "3":
            atualizar_equipamento()
        elif opcao == "4":
            excluir_equipamento()
        elif opcao == "5":
            maior_custo()
        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Execução do programa
if __name__ == "__main__":
    menu()