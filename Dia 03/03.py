# Dia 03 - Conditional Statements, Logical Operations, Code Blocks and Scope
"""If Else

Condicionais para checar o que devemos mandar o código fazer em cada caso

"""

print("Bem vindo a montanha-russa!")
altura = int(input("Qual sua altura? "))  # Não esquecer de converter para int

if altura >= 120:
    print("Bem vindo, pode entrar!")
else:
    print("Vê se cresce!")

print("Bem vindo ao mundo dos programadores!")
programador = "Sim"

resposta = input("Você é programador? Sim Não ")

if programador == resposta:
    print("Bem vindo a nossa sala de programadores!")
else:
    print("Você precisa ser um programador!")


"""
Modulo operator

%

Pega o resto da operação

print(10 % 3)

No caso, o resultado será 1

10 / 3 = 3 e resta 1


print(55 % 8)

O resultado será 7

55 / 8 = 6 e resta 7

"""


"""
Checar se é número par ou ímpar

"""
numero_a_verificar = int(input("Qual número você quer testar? "))
if numero_a_verificar % 2 == 0:
    print("Esse é um número par")
else:
    print("Esse um número ímpar")


# Checagem de ingresso para o exemplo da montanha russa
# Montar uma checagem de idade: Menores de 18 pagam R$7 / Maiores pagam R$12 e idosos pagam R$2

# Checagem de ingresso para o exemplo da montanha russa
# Montar uma checagem de idade: Menores de 18 pagam R$7 / Maiores pagam R$12 e idosos pagam R$2


# Checagem de ingresso para o exemplo da montanha russa
# Montar uma checagem de idade: Menores de 18 pagam R$7 / Maiores pagam R$12 e idosos pagam R$2


print("Bem vindo a montanha-russa!")
altura = int(input("Qual sua altura? "))  # Não esquecer de converter para int

if altura >= 120:
    idade = int(
        input("Ótimo, apenas uma pergunta. Qual tua idade? ")
    )  # Novamente, não esquecer de converter para int
    if idade < 18:
        # como a entrada é diferente de acordo com a idade, eu declaro elas de acordo com cada idade
        entrada = 7
        print(f"Você paga R${entrada}")
    elif idade > 17 and idade < 65:
        entrada = 12
        print(f"Você paga R${entrada}")
    elif idade >= 65:
        entrada = 2
        print(f"Você paga R${entrada}")
    quer_foto = input("Quer uma foto de recordação? Sim Não")
    # verificando se a pessoa quer uma foto, se quiser, adicionaremos + 3
    if quer_foto == "Sim":
        # Aqui declaramos que se a pessoa quiser uma foto, o valor da entrada passa a ser a entrada + 3
        entrada += 3
        print(f"Então vai ficar R$ {entrada}!")
    else:
        print(f"Então será apenas {entrada} mesmo, obrigado!")
else:
    print("Desculpe, você precisa ter 120cm ou mais")

"""
Criar um programa de pedido de pizzas

Esse programa deve ser capaz  de oferecer três tamanhos
Perguntar se quer peperoni extra na pizza
Perguntar se quer queijo extra
Precificar de acordo com as escolhas

Pizza Pequena: R$15
Pizza Média: R$20
Pizza Grande:R$$25

Peperoni extra na pizza pequena: R$2
Peperoni extra na pizza média ou grande: R$3

Queijo extra na pizza: R$1



"""

print("Bem vindo a Lorenzo's Pizzas")
size = input("Qual o tamanho da pizza? P M G ")
peperoni = input("Quer peperoni extra? ")
queijo_extra = input("Quer queijo extra? ")
preco = 0

# bloco para verificar o tamanho

if size == "P":
    preco += 15
elif size == "M":
    preco += 20
elif size == "G":
    preco += 25

# bloco para queijo
if queijo_extra == "Sim":
    preco += 2

# bloco para peperoni
if peperoni == "Sim" and size != "P":
    preco += 3
elif peperoni == "Sim" and size == "P":
    preco += 2

print(f"O preço da pizza é {preco}")


"""

Crie um jogo de caça ao tesouro

Primeira opção = Esquerda ou direita (esquerda Game Over)

Segunda opção = Nadar ou esperar (nadar Game Over)

Escolher uma porta =

Azul - Game Over
Vermelha - Game Over
Amarela - Tesouro

"""

print("Bem vindo a caça ao tesouro do vovô em Stardew Valley\n")
direcao = input(
    "Você está na entrada da olha gengibre. Você vai a direita ou esquerda?\n"
).upper()  # A função .upper() transforma tudo em maiusculo. Assim, não importa como seja digitado, semper será aceito
if direcao == "direita":
    print("Você morreu devorada pelos crododilos. GAME OVER\n")
else:
    print("Parabéns! Você pegou o barco de volta para a vila!\n")

nadar_esperar = input(
    "O Willy não está aqui! Você quer tentar nada ou esperar? \n"
).upper()  # A função .upper() transforma tudo em maiusculo. Assim, não importa como seja digitado, semper será aceito
if nadar_esperar == "Nadar":
    print("Você morreu devorada pelos crododilos. GAME OVER\n")
else:
    print("Pouco depois ele chegou e te levou de volta para Stardew\n")

porta = input(
    "Finalmente você chegou em casa! Logo que você chegou em casa, apareceram três portas. É o teste final, qual porta você escolhe: Azul Vermelha Amarela \n"
).upper()

if porta != "AMARELA":
    print("Apareceu uma bruxa e você morreu. GAME OVER\n")
else:
    print(
        "\nParabéns, você encontrou o tesouro. Você sente a mão do vovô afagar teu ombro. Bom trabalho, meu neto!\n"
    )
