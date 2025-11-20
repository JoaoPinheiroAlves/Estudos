#Entrada de dados do usuário (input)
nome = input("Qual seu nome? ")
print("Olá,", nome)
#Exemplo de entrada e saída de dados em Python.
#Importante: tudo que vem do input() é string, mesmo que seja número.

#Convertendo tipos (type casting)
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print("Daqui 10 anos você terá", idade + 10, "anos")
#Aqui convertemos a entrada para inteiro e float para fazer cálculos.

#Operadores de comparação (importante para if/else)
a = 10
b = 5
print(a > b)   # maior que
print(a < b)   # menor que
print(a == b)  # igual a
print(a != b)  # diferente de
print(a >= b)  # maior ou igual a
print(a <= b)  # menor ou igual a
#Esses operadores retornam True ou False.

#exemplo de uso em if/else
senha = "1234"
digito = input("Digite a senha: ")

if digito == senha:
    print("Acesso liberado!")
else:
    print("Senha incorreta!")

#Loops avançados (for com enumerate e range)
frutas = ["maçã", "banana", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)
#saida:
#0 maçã
#1 banana  
#2 uva

#range com início, fim e passo
for i in range(1, 11, 2):
    print(i)

#isso imrpime:
1, 3, 5, 7, 9

#Funções com retorno (return)
def soma(a, b):
    return a + b
resultado = soma(3, 5)
print("A soma é:", resultado)  # Imprime "A soma é: 8"

#Funções com múltiplos retornos
def calcular(valores):           # Define uma função chamada 'calcular' que recebe uma lista chamada 'valores'
    soma = sum(valores)          # 'sum' soma todos os elementos da lista e guarda em 'soma'
    maior = max(valores)         # 'max' retorna o maior valor da lista
    menor = min(valores)         # 'min' retorna o menor valor da lista
    return soma, maior, menor    # Retorna três valores: soma, maior número e menor número

soma_total, maior_num, menor_num = calcular([3, 7, 1, 9])  
# Chama a função 'calcular' passando a lista [3, 7, 1, 9]
# Os três valores retornados são atribuídos às variáveis:
# soma_total → soma dos números
# maior_num  → maior número da lista
# menor_num  → menor número da lista

print("Soma:", soma_total)       # Imprime o texto "Soma:" e o valor da variável soma_total
print("Maior:", maior_num)       # Imprime "Maior:" e o maior número encontrado
print("Menor:", menor_num)       # Imprime "Menor:" e o menor número encontrado

#struturas de repetição com condição de saída
while True:  
    # Inicia um loop infinito. O código dentro dele vai repetir para sempre
    # até que um 'break' seja executado.
    comando = input("Digite 'sair' para encerrar: ")  
    # Mostra uma mensagem pedindo para o usuário digitar algo
    # e guarda a resposta na variável 'comando'.
    if comando.lower() == 'sair':  
        # Verifica se o texto digitado, transformado para minúsculas,
        # é exatamente igual a 'sair'.
        print("Encerrando o programa.")  
        # Mostra a mensagem de encerramento.
        break  
        # Interrompe o loop e termina o programa.
    else:  
        # Caso o usuário NÃO tenha digitado 'sair':
        print("Você digitou:", comando)  
        # Mostra na tela o que o usuário escreveu.

print("Fim do exercício!")  # Imprime uma mensagem final