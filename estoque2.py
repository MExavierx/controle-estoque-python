estoque = {} 

try: 
    with open ("estoque.txt", "r") as arquivo: 
        for linha in arquivo:
            produto, quantidade = linha.strip().split(",")
            estoque[produto] = int(quantidade)
except FileNotFoundError:
    pass

while True: 
    print("\n ====== CONTROLE DE ESTOQUE ======")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Ver estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opçao: ")

    if opcao == "1": 
        produto = input("Insira o nome do produto: ").upper().strip()
        quantidade = int(input("Insira a quantidade: "))

        if produto in estoque: 
            estoque[produto] += quantidade
        else: 
            estoque[produto] = quantidade

            print("\nProduto adicionado!")
    
    elif opcao == "2": 
        produto = input("Insira o nome do produto que deseja remover: ").upper().strip()
        quantidade = int(input("Insira a quantidade que deseja remover: "))

        if produto in estoque: 
            if estoque[produto] >= quantidade:
                estoque[produto] -= quantidade
                if estoque[produto] == 0:
                    del estoque[produto]
                    print(f"{produto} removido do estoque.")
                else:
                    print("Produto removido!")
                    print(f"Estoque atual de {produto}: {estoque[produto]}")
            else: 
                print("Estoque insuficiente! ")
        else: 
            print("Produto não encontrado")

    elif opcao == "3": 
        if estoque: 
            print("\nProdutos no estoque: ")
            for produto, qtd in estoque.items(): 
                print(f"{produto} - {qtd}")

        else: 
            print("Estoque vazio")

    elif opcao == "4":
        with open("estoque.txt" , "w") as arquivo: 
            for produto, quantidade in estoque.items():
                arquivo.write(f"{produto}, {quantidade}\n")
        print("Saindo...")
        break
    else: 
        print("Opção inválida")