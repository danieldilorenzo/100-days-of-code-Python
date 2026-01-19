# Dia 05 - Python Loops

"""
Projeto do dia: Criar um gerador de senhas

"""

"""
For Loop

for item in list of item:
# faça algo com cada item


"""

iniciais = ["Bulbasaur", "Chamander", "Squirtle"]

# para cada poke na lista iniciais
for poke in iniciais:
    print(poke)

    # Vai printar cada pokemon na lista seguido de " Mega"
    print(poke + " Mega")
print(iniciais)

"""
notar como a indentação é importante.

No caso acima ele executou primeiro o for, depois o print iniciais, pois entendeu que  o comando era primeiro


for poke in iniciais:
    print(poke)
    print(poke + " Mega")

E depois    
    
print(iniciais)

Se o comando acima, estivesse na mesma indentação, o computador entenderia que ele estaria junto com o for

"""


numeros = [1, 3, 5, 7, 9]

# forma mais fácil de se somar
# total = sum(numeros)
# print(total)


inicio = 0
for numerozinho in numeros:
    inicio += numerozinho

print(inicio)


# Outra forma de somar
#
# mandando outra lista de números
numeros_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

total = 0

# para cada número dentro da lista
for score in numeros_2:
    # pegue o total e some um número
    total += score

print(total)


numeros = [10, 2, 8, 20, 34, 89, 50, 48, 6, 7, 77, 90, 16, 21, 24, 35, 63]

# setando o máximo para 0
maximo = 0

# para os aleatorios na lista numeros
for aleat in numeros:
    # se o número aleatorio for maior que o número máximo
    if aleat > maximo:
        # o número aleatorio em questão passa a ser o máximo
        maximo = aleat

# ele vai fazendo essa verificação para todos os números, a fim de encontrar o número máximo

print(maximo)


# Como contar de 1 a 100

total = 0

# ele vai pegar de 1 a 100 (se fosse 'in range(1,100)', ele pegaria de 1 a 99)
for numeros in range(1, 101):
    # total é igual a 0 mais a soma de cada número
    total += numeros

print(total)


## Gerador de senhas

import random

letras = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
    "y",
    "w",
    "z",
]
numbers = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
caracteres = ["!", "$", "@", "%", "&", "(", ")", "*", "+"]
senha = ""
print("Bem vindo ao gerador de senhas")
nr_letras = int(input("Quantas letras você quer? "))
nr_numeros = int(input("Quantos números você quer? "))
nr_caracteres = int(input("Quantos caracteres você quer? "))

# Para cada letra (no caso, chamada de cada) entre 1 e o
# número que escolhemos (lembrando que ele sempre pega um
# número abaixo, então temos que adicionar 1)
for cada in range(1, nr_letras + 1):
    # Pegar a senha e randomizar a quantidade de letras que escolhemos
    senha += random.choice(letras)
for cada in range(1, nr_numeros + 1):
    senha += random.choice(numbers)
for cada in range(1, nr_caracteres + 1):
    senha += random.choice(caracteres)


print(senha)


# Gerador de senhas randomizado

import random

letras = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
    "y",
    "w",
    "z",
]
numbers = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
caracteres = ["!", "$", "@", "%", "&", "(", ")", "*", "+"]
# definindo a senha como uma lista para ser possível a randomização depois
password_list = []
print("Bem vindo ao gerador de senhas")
nr_letras = int(input("Quantas letras você quer? "))
nr_numeros = int(input("Quantos números você quer? "))
nr_caracteres = int(input("Quantos caracteres você quer? "))

# Para cada letra (no caso, chamada de cada) entre 1 e o
# número que escolhemos (lembrando que ele sempre pega um
# número abaixo, então temos que adicionar 1)
for cada in range(1, nr_letras + 1):
    # Pegar a senha e randomizar a quantidade de letras que escolhemos
    # usando append para ele anexar na lista
    password_list.append(random.choice(letras))
for cada in range(1, nr_numeros + 1):
    password_list.append(random.choice(numbers))
for cada in range(1, nr_caracteres + 1):
    password_list.append(random.choice(caracteres))
# Mandando randomizar
# (o random só funciona em lista!!!)
random.shuffle(password_list)

# Redefinindo a senha final em string
senha_final = ""
for char in password_list:
    senha_final += char

print(f"Sua senha é {senha_final}")
