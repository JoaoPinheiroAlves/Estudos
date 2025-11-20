# Sistema de Cadastro e Análise de Alunos - Aula 2

# Função que analisa as notas e retorna múltiplos valores
def analisar_notas(notas):
    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    return media, maior, menor, situacao


# Lista principal onde os alunos serão armazenados
alunos = []


# Função para cadastrar um novo aluno
def cadastrar_aluno():
    print("\n=== Cadastro de Aluno ===")
    
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))

    # Recebendo 3 notas
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    # Analisando as notas
    media, maior, menor, situacao = analisar_notas(notas)

    # Salvando tudo num dicionário
    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas,
        "media": media,
        "maior": maior,
        "menor": menor,
        "situacao": situacao
    }

    alunos.append(aluno)
    print(f"\nAluno {nome} cadastrado com sucesso!\n")


# Função para listar todos os alunos cadastrados
def listar_alunos():
    if not alunos:
        print("\nNenhum aluno cadastrado ainda.\n")
        return

    print("\n=== Lista de Alunos ===")
    for indice, aluno in enumerate(alunos):
        print(f"\nAluno {indice + 1}:")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f}")
        print(f"Maior Nota: {aluno['maior']}")
        print(f"Menor Nota: {aluno['menor']}")
        print(f"Situação: {aluno['situacao']}")
    print()


# MENU PRINCIPAL (while True + break)
def menu():
    while True:
        print("=== Sistema de Alunos ===")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            print("Saindo... Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# Inicia o programa
menu()
