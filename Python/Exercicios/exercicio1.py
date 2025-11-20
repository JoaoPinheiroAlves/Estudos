# Variáveis armazenam informaçõe
nome = "Victor"   # string
idade = 18        # inteiro
altura = 1.75     # float (número com vírgula)

# vVocê pode imprimir elas:
print("Meu nome é", nome, "e tenho", idade, "anos")

# Operações matemáticas
a = 10
b = 5

print(a + b)  # soma
print(a - b)  # subtração
print(a * b)  # multiplicação
print(a / b)  # divisão
print(a // b)  # divisão inteira
print(a % b)  # resto da divisão
print(a ** b)  # potência

# Estruturas de decisão (if/else)
idade = 18

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
# Atenção ao espaçamento: Python usa indentação para organizar o código (não usa {})

# Estruturas de repetição (for / while)
for i in range(5):
    print("Número:", i)
# Isso imprime números de 0 a 4
# Exemplo com while:
contador = 0
while contador < 5:
    print("Contador =", contador)
    contador += 1  # contador = contador + 1
# Isso também imprime números de 0 a 4

# Funções


def saudacao(nome):
    print("Olá,", nome)


saudacao("Maria")  # Chama a função com o argumento "Maria"
saudacao("João")   # Chama a função com o argumento "João"
# Isso imprime "Olá, Maria" e "Olá, João"

# Listas
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Imprime "maçã"
frutas.append("uva")  # Adiciona "uva" à lista
print(frutas)  # Imprime a lista atualizada
for fruta in frutas:
    print("Eu gosto de", fruta)
# Isso imprime cada fruta na lista

# Dicionários
pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
print(pessoa["nome"])  # Imprime "Ana"
pessoa["idade"] = 26  # Atualiza a idade
print(pessoa)  # Imprime o dicionário atualizado
for chave, valor in pessoa.items():
    print(chave + ":", valor)
# Isso imprime cada chave e valor no dicionário

# Comentários
# Comentários são linhas que o Python ignora
# Eles são úteis para explicar o código
print("Fim do exercício!")  # Imprime uma mensagem final
