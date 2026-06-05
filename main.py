#Sistema de Gerenciamento de Biblioteca que permite:
'''● Cadastrar novos livros e usuários.
● Emprestar e devolver livros.
● Pesquisar livros e usuários.
● Listar livros disponíveis e emprestados.
● Gerar relatórios de empréstimos.
● Persistir dados em arquivos para garantir que as informações sejam mantidas entre
as execuções do programa.
● Testar funcionalidades para garantir a confiabilidade do sistema.'''

from biblioteca import GerenciadorBiblioteca

sistema = GerenciadorBiblioteca()

while True:

    print('_______BEM-VINDO!______')
    print('Opção 1: Bibliotecario')
    print('Opção 2: Cliente')
    print('Opção 3: Sair')

    opcao_principal = input('\nInforme qual o seu acesso: ')

    if opcao_principal == '1':
        opcao1 = ''
        while opcao1 != '5':
            print('Opção 1: Cadastrar um livro')
            print('Opção 2: Pesquisar Usuarios cadastrados')
            print('Opção 3: Listar Livros Emprestados')
            print('Opção 4: Salvar')
            print('Opção 5: Sair')

            opcao1 = input('\nEscolha uma opção: ')

            if opcao1 == '1':
                print('\n___CADASTRO DE LIVRO___')
                titulo = input('Título: ')
                autor = input('Autor: ')
                ano = input('Ano: ')
                ibsn = input('IBSN: ')
                sistema.cadastrar_livro(titulo, autor, ano,ibsn)
                print('Livro cadastrado com sucesso!')
            
            elif opcao1 == '2':
                print('\n___PESQUISAR USUÁRIO___')
                termo = input('Digite o nome do usuario que deseja buscar: ')

                usuario_encontrado = sistema.pesquisar_usuario(termo)
                if len(usuario_encontrado) == 0:
                    print('Não temos nenhum usuário com esse nome no momento!')
                else:
                    print('-' * 40)
                    for user in usuario_encontrado:
                        print(f"ID: {user.id_usuario} | Nome: {user.nome} | Contato: {user.telefone}")
                    print('-' * 40)  

            elif opcao1 == '3':
                print('\n___LIVROS EMPRESTADOS NO MOMENTO___')
                livros_ocupados = sistema.listagem_livros_emprestados()
                
                if len(livros_ocupados) == 0:
                    print('Nenhum livro emprestado no momento. Todos estão na prateleira!')
                else:
                    print('-' * 40)
                    for livro in livros_ocupados:
                        print(f"ID: {livro.id_livro} | Título: {livro.titulo}")
                    print('-' * 40)
            
            elif opcao1 == '4':
                sistema.salvar_dados()
                print('Dados salvos com sucesso no disco!\n')
           
            elif opcao1 == '5':
                print('Encerrando o sistema...')
                break
            
            else:
                print('Opção invalida!')

    elif opcao_principal == '2':
        opcao2 = ''
        while opcao2 != '7':
            print('Opção 1: Cadastrar')
            print('Opção 2: Pesquisar Livros Disponiveis')
            print('Opção 3: Listar Livro')
            print('Opção 4: Pegar Livro Emprestado')
            print('Opção 5: Devolver Livro')
            print('Opção 6: Salvar')
            print('Opção 7: Sair')

            opcao2 = input('\nEscolha uma opção: ')    

            if opcao2 == '1':
                print('\n___CADASTRO DE USUARIO___')
                nome = input('Nome: ')
                email = input('E-mail: ')
                telefone = input('Telefone: ')
                id_recebido = sistema.cadastrar_usuario(nome, email, telefone)
                print(f'Cadastro concluído! Anote o seu ID de acesso: {id_recebido}')
            
            elif opcao2 == '2':
                print('\n___PESQUISAR LIVROS___')
                termo = input('Digite o titulo do livro que deseja buscar: ')

                livro_encontrado = sistema.pesquisar_livro(termo) 
                if len(livro_encontrado) == 0:
                    print('Não temos nenhum livro com esse titulo no momento!')
                else:
                    print('-' * 40)
                    for info in livro_encontrado:
                        print(f"ID: {info.id_livro} | Titulo: {info.titulo} | Autor: {info.autor}")
                    print('-' * 40)  
                
            elif opcao2 == '3':
                print('\n___CATÁLOGO DE LIVROS DISPONÍVEIS___')
                livros_prateleira = sistema.listagem_livros()
                if len(livros_prateleira) == 0:
                    print('Não temos nenhum livro disponivel no momento!')
                else:
                    print('Anote o ID do livro que queira pegar.')
                    print('-' * 40)
                    for livro in livros_prateleira:
                        print(f"ID: {livro.id_livro} | Título: {livro.titulo} | Autor: {livro.autor}")
                    print('-' * 40)
            
            elif opcao2 == '4':
                print('\n--- EMPRÉSTIMO DE LIVRO ---')
                id_cliente = input('Informe o seu ID: ')
                id_livro_desejado = input('Informe o ID do livro desejado: ')
                sucesso = sistema.empresta_livros(id_cliente, id_livro_desejado) 

                if sucesso == True:
                    print('Emprestimo realizado com sucesso;')
                else:
                    print('Falha no emprestimo verifique se os IDs estão corretos ou se o livro está disponivel.')
           
            elif opcao2 == '5':
                print('\n--- DEVOLUÇÃO DE LIVRO ---')
                id_recebido = input('Informe o ID do emprestimo: ')
                
                sucesso = sistema.devolucao_livros(id_recebido) 
                if sucesso == True:
                    print('Livro devolvido com sucesso, obrigado')
                else:
                    print('Falha na devolução verifique se o ID do emprestimo está correto.')
            
            elif opcao2 == '6':
                sistema.salvar_dados()
                print('Dados salvos com sucesso no disco!\n')
            
            elif opcao2 == '7':
                print('Encerrando o sistema...')  
            
            else:
                print('Opção invalida!')   
    
    elif opcao_principal == '3':
        print('\nEncerrando o sistema, obrigado por visitar a biblioteca!\n')
        break
    else:
        print('Opção invalida!')

