# Mini Agenda de Contatos- Aula 1

# Lista para armazenar os contatos
contatos = []

# Função para adicionar contato


def adicionar_contato():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")
    contato = {"nome": nome, "idade": idade, "cidade": cidade}
    contatos.append(contato)
    print(f"{nome} foi adicionado(a) à agenda!\n")

# Função para mostrar todos os contatos


def listar_contatos():
    if not contatos:
        print("Nenhum contato na agenda.\n")
        return
    print("Lista de Contatos:")
    for i, c in enumerate(contatos):
        print(f"{i+1}. {c['nome']} - {c['idade']} anos - {c['cidade']}")
    print()

# Função para atualizar um contato


def atualizar_contato():
    listar_contatos()
    if not contatos:
        return
    indice = int(
        input("Digite o número do contato que deseja atualizar: ")) - 1
    if 0 <= indice < len(contatos):
        novo_nome = input("Novo nome: ")
        nova_idade = int(input("Nova idade: "))
        nova_cidade = input("Nova cidade: ")
        contatos[indice] = {"nome": novo_nome,
                            "idade": nova_idade, "cidade": nova_cidade}
        print("Contato atualizado!\n")
    else:
        print("Contato inválido!\n")

# Função para excluir um contato


def excluir_contato():
    listar_contatos()
    if not contatos:
        return
    indice = int(input("Digite o número do contato que deseja excluir: ")) - 1
    if 0 <= indice < len(contatos):
        nome = contatos[indice]["nome"]
        contatos.pop(indice)
        print(f"{nome} foi removido(a) da agenda!\n")
    else:
        print("Contato inválido!\n")

# Menu principal


def menu():
    while True:
        print("=== Mini Agenda de Contatos ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Atualizar contato")
        print("4. Excluir contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        print()
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            atualizar_contato()
        elif opcao == "4":
            excluir_contato()
        elif opcao == "5":
            print("Saindo da agenda. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.\n")


# Executa o menu
menu()
