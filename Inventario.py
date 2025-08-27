inventario = []

while True:
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar iventário")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome do item: ")
        quantidade = input("Quantidade: ")
        item = {"nome": nome, "quantidade": quantidade}
        inventario.append(item)
        print("Item adicionado.")
        
    elif opcao == "2":
        nome = input("Nome do item para remover: ")
        achou = False
        for item in inventario:
            if item["nome"] == nome:
                inventario.remove(item)
                achou = True
                print("Item removido.")
                break
        if not achou:
            print("Item não encontrado")  

    elif opcao == "3":
        if len(inventario) == 0:
            print("Iventário vazio.")
        else:
            for item in  inventario:
                print(item) 
                      
    elif opcao == "4":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")
        