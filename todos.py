# Função para imprimir texto colorido no terminal
def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Exercício 1: Soma de dois números
print_color("Exercício 1: Soma de dois números", "34")  # Azul
n = float(input("Insira o 1º número desejado: "))
n1 = float(input("Insira o 2º número desejado: "))
soma = n + n1
print(f"A soma dos números é: {soma}")
print("-----------------------")

# Exercício 2: Verifica se o número é par ou ímpar
print_color("Exercício 2: Verifica se o número é par ou ímpar", "32")  # Verde
num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")
print("-----------------------")

# Exercício 3: Determina o maior entre três números
print_color("Exercício 3: Determina o maior entre três números", "35")  # Amarelo
num = float(input("Digite o primeiro número: "))
num1 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num > num1 and num > num3:
    print(f"O número {num} é maior")
elif num1 > num and num1 > num3:
    print(f"O número {num1} é maior")
else:
    print(f"O número {num3} é maior")
print("-----------------------")

# Exercício 4: Contagem de 1 a 10
print_color("Exercício 4: Contagem de 1 a 10", "36")  # Ciano
input("Digite qualquer tecla para começar: ")
for num in range(1, 11):
    print(num)
print("-----------------------")

# Exercício 5: Tabuada
print_color("Exercício 5: Tabuada", "33")  # Verde claro
num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("-----------------------")

# Exercício 6: Verifica maioridade
print_color("Exercício 6: Verifica maioridade", "31")  # Verde escuro
while True:
    idade = int(input("Digite a sua idade: "))
    if idade == 0:
        print("Processo encerrado")
        break
    if idade >= 18:
        print("Maior de Idade!")
    else:
        print("Menor de Idade")
print("-----------------------")

# Exercício 7: Soma de números pares de 1 a 100
print_color("Exercício 7: Soma de números pares de 1 a 100", "37")  # Branco
soma = 0
for num in range(2, 101, 2):
    soma += num
print(f"A soma dos números pares de 1 a 100 é: {soma}")
