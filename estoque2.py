# dicionário que vai armazenar os produtos e as quantidades
estoque = {} 

# tenta carregar o estoque que ficou salvo antes no arquivo
try: 
    with open ("estoque.txt", "r") as arquivo: 
        #vai "ler" cada linha do arquivo 
        for linha in arquivo:
            #separa o nome do produto e a quantidade usando a virgula
            produto, quantidade = linha.strip().split(",")

            #adiciona o produto ao dicionario, convertendo a quantidade para número
            estoque[produto] = int(quantidade)
#se o arquivo não existir, o programa continua rodando 
except FileNotFoundError:
    pass

#loop principal do programa (menu do sistema de controle)
while True: 
    print("\n ====== CONTROLE DE ESTOQUE ======")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Ver estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opçao: ")

    if opcao == "1": 
        #recebe o nome do produto e padroniza ele para evitar erros de digitação ou utilização de espaços 
        produto = input("Insira o nome do produto: ").upper().strip()
        #recebe a quantidade e converte para número inteiro 
        quantidade = int(input("Insira a quantidade: "))
        #verifica se o produto existe no estoque
        if produto in estoque: 
            estoque[produto] += quantidade
        else: 
            estoque[produto] = quantidade

            print("\nProduto adicionado!")
    
    elif opcao == "2": 
        #em todas as linhas que são recebidos o nome do produto, tem a padronização 
        produto = input("Insira o nome do produto que deseja remover: ").upper().strip()
        quantidade = int(input("Insira a quantidade que deseja remover: "))

        if produto in estoque: 
            #verifica se tem a quantidade suficiente e depois subtrai 
            if estoque[produto] >= quantidade:
                estoque[produto] -= quantidade
                if estoque[produto] == 0: #se o estoque chegar a 0 ele remove o produto 
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
            for produto, qtd in estoque.items(): # se tiver produtos no nosso arquivo vai retornar pares (produto, quantidade)
                print(f"{produto} - {qtd}")

        else: 
            print("Estoque vazio")

    elif opcao == "4":
        with open("estoque.txt" , "w") as arquivo: # reescreve com o novo estoque
            for produto, quantidade in estoque.items():
                arquivo.write(f"{produto}, {quantidade}\n")
        print("Saindo...")
        break
    else: 
        print("Opção inválida")