def menu_principal():
    exibir_subtitulo('Selecione uma das opções: ')
    print('1. Cadastre-se')
    print('2. Login ')
    print('3. Cadastrar Empresa')
    print('4. Login Empresa')
    print('5. Cadastrar Colaborador')
    print('6. Login Colaborador')
    print('9. Sair')

def menu_empresa():
    opcao = 0
    while opcao != 4:
        exibir_nome()
        exibir_subtitulo('Menu cliente')
        print('1. Cadastrar produtos')
        print('2. Ver produtos')
        print('3. Relatório')
        print('4. Sair')
        opcao = int(input('Escolha uma opção:'))
        if opcao == 1:
            cad_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            gerar_relatorio()
        elif opcao not in [1, 2, 3, 4]:
            print('Opção inválida!')
            input("Pressione ENTER para continuar...")

def menu_cliente():
    opcao = 0
    while opcao != 9:
        exibir_subtitulo('Menu cliente')
        print('1. Ver Produtos disponiveis')
        print('2. Buscar produtos')
        print('3. Ver empresas cadastradas')
        print('4. Atualizar dados')
        print('5. Carrinho')
        print('6. Ver pedidos anteriores')
        print('9. Sair')
        opcao = int(input("Opcao:"))
        if opcao == 1:
            ver_produtos()
        elif opcao == 2:
            busca_produto()
        elif opcao == 3:
            ver_empresas()
        elif opcao == 4:
            atualizar_cliente()
        elif opcao == 5:
            menu_carrinho()
        elif opcao == 6:
            ver_pedidos()
        elif opcao not in [1, 2, 3, 4, 5, 6, 9]:
            print('Opção inválida!')
            input("Pressione ENTER para continuar...")



def menu_carrinho():
    opcao = 0
    while opcao != 9:
        exibir_subtitulo('Digite uma das opções')
        print('1. Adicionar produto ao carrinho')
        print('2. Ver Carrinho')
        print('3. Remover produto do Carrinho')
        print('4. Editar produto do Carrinho')
        print('5. Finalizar pedido')
        print('9. Sair')
        opcao = int(input("Opcao:"))
        if opcao == 1:
            adicionar_carrinho()
        elif opcao == 2:
            ver_carrinho()
        elif opcao == 3:
            remover_carrinho()
        elif opcao == 4:
            print('Em breve')
        elif opcao == 5:
            finalizar_pedido()
        elif opcao not in [1, 2, 3, 4, 5, 9]:
            print('Opção inválida!')
            input("Pressione ENTER para continuar...")
