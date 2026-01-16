# Dia 04 - Randomisation and Python Lists

"""

Para randomizar números, primeiro temos que importar a biblioteca que randomiza, que deve sempre ser colocada no início da página

import random


"""

import random
import modulo_dan
import poke251


"""
Nós podemos também criar um módulo, onde guardamos funções que sempre vamos usar, para não ter que ficar digitando o tempo todo

Criei um módulo chamado modulo_dan.py onde coloquei meu numero favorito como 6

Importei ele no início do documento, setando o nome (e se necessário, o caminho)

"""

# print(modulo_dan.num_favorito)


# randint randomiza um número inteiro entre os valores que escolhemos (no caso, 1 a 10)
num_aleatorio = random.randint(1, modulo_dan.num_favorito)
print(num_aleatorio)

# random.random() serve para randomizar números decimais entre 0 e 1 - Não sendo possível escolher um intervalo
random_0ou1 = random.random()
print(random_0ou1)

# random.random() serve para randomizar números flutuante (no caso, de 0 a 20)
random_float = random.uniform(0, 20)
print(random_float)

"""
Criar um programa de cara ou coroa

"""

resultado = random.randint(1, 2)
if resultado == 1:
    print("Cara")
else:
    print("Coroa")


"""
Listas em Python sempre começa e termina com []

"""
starters_poke = ["Bulbasaur", "Charmander", "Squirtle"]
# escolha = random(starters_poke)
print(starters_poke[0])
print(starters_poke[1])
# O "\n" é para ficar mais fácil de ver no terminal
print(starters_poke[2], "\n")

# Mudando o nome do inicial 1
starters_poke[1] = "Cyndaquil"

print(starters_poke[0])
print(starters_poke[1])
# O "\n" é para ficar mais fácil de ver no terminal
print(starters_poke[2], "\n")

# Eu estou cirando um pokemon!
starters_poke.append("Daniel Di Lorenzo")
print(starters_poke)
# Verificando qual é o último pokemon na lista (EU!!!)
print(starters_poke[-1])

# Adicionando mais Pokemons na lista (não esquecer dos [])
starters_poke.extend(["Chikorita", "Charmander", "Totodile"])
print(starters_poke)

# Eu deixando de ser um pokemon
starters_poke.remove("Daniel Di Lorenzo")

# Imprimindo novamente a lista de Pokemons para mostrar que eu não estou mais na lista
print(starters_poke)
escolhido = random.choice(starters_poke)
print(f"Teu pokemon será {escolhido}!")


"""
Outra opção, é criar uma função que cria números aleatórios, e  mandar escolher da lista, o número referente ao aleatório gerado
"""
# Criando a função que gera um numero aleatório
num_aleatorio = random.randint(0, 5)
print(num_aleatorio)

# print da lista starters_poke, o pokemon referente ao número que saiu
print(starters_poke[num_aleatorio])

# Eu criei um módulo externo com os 251 primeiros pokemons, e fiz um randomizador de time, puxando esse módulo externo
meu_time = random.sample(poke251.pokemons251, 6)
print(f"Seu time será {meu_time}")

###

pokemons = ["Bulbasaur", "Charmander", "Squirtle"]
gen2 = ["Chikorita", "Cyndaquil", "Totodile"]


# No exemplo abaixo, criei uma lista juntando as duas listas anteriores
# Print: da lista todos (a nova lista), pegar a lista 1 e imprimir o pokemon 1 (no caso, Cyndaquil)
todos = [pokemons, gen2]
print(todos[1][1])


"""
Criar um jogo de Pedra, Papel ou Tesoura


"""

# Rock
pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


# Paper
papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

randomPPT = random.randint(0, 2)
print("Bem vindo a brincadeira de Pedra, Papel ou Tesoura!\n")
escolha = input("Escolha entre Pedra, Papel ou Tesoura: ").upper()
# escolha_errada = escolha != "PEDRA" and escolha != "PAPEL" and escolha != "TESOURA"

# Antes eu estava errado, porque eu estava colocando as condicionais com or. Nesse caso, tem que ser and
# Se for uma escolha errada, printa o erro, dá a escolha da máquina e manda jogar direito
if escolha != "PEDRA" and escolha != "PAPEL" and escolha != "TESOURA":
    print(" ")
    print(f"Escolha uma opção correta\n")

# Se for escolha certa, executa esse bloco. Se for escolha errada, pula direto para a máquina
if escolha == "PEDRA":
    print(f"Você escolheu:\n {pedra}")
elif escolha == "PAPEL":
    print(f"Você escolheu:\n {papel}")
elif escolha == "TESOURA":
    print(f"Você escolheu:\n {tesoura}")

if randomPPT == 0:
    print(f"A máquina escolheu:\n {pedra}")
elif randomPPT == 1:
    print(f"A máquina escolheu:\n {papel}")
elif randomPPT == 2:
    print(f"A máquina escolheu:\n {tesoura}")

# Condicionais para PEDRA
if escolha == "PEDRA" and randomPPT == 0:
    print("Empate")
elif escolha == "PEDRA" and randomPPT == 1:
    print("Derrota")
elif escolha == "PEDRA" and randomPPT == 2:
    print("Vitória")

# Condicionais para PAPEL
if escolha == "PAPEL" and randomPPT == 0:
    print("Vitória")
elif escolha == "PAPEL" and randomPPT == 1:
    print("Empate")
elif escolha == "PAPEL" and randomPPT == 2:
    print("Derrota")

# Condicionais para TESOURA
if escolha == "TESOURA" and randomPPT == 0:
    print("Derrota")
elif escolha == "TESOURA" and randomPPT == 1:
    print("Vitória")
elif escolha == "TESOURA" and randomPPT == 2:
    print("Empate")

# Antes eu estava errado, porque eu estava colocando as condicionais com or. Nesse caso, tem que ser and
if escolha != "PEDRA" or escolha != "PAPEL" or escolha != "TESOURA":
    print("Você não soube jogar e perdeu!")
