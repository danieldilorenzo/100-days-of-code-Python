# Dia 06 - Funções Python
import random

"""

Definindo e chamando funções

print('Hello world') #print é uma função

len("Olá")  # len é uma função

"""


# vamos criar a nossa própria função
# no caso, uma função que printa oi
# e em seguida, printa tchau
def teste():
    print("Oi")
    print("Tchau")


# no caso, para executar, podemos apenas chamar ela simplesmente
# teste()

# para repetir uma função 5 vezes
for função in range(5):
    teste()

"""

Indentação

"""


def hw():
    print("Hello")
    print("World")
    print(" ")


for ola in range(3):
    hw()


# Saber como está o céu!!!

ceu = int(input("Como está o ceu?\n (1) Azul\n (2) Cinza\n (3) Chovendo\n\n "))


def condicao_ceu():
    if ceu == 1:
        print("\nEntão o clima está bom e o céu azul!")
    if ceu == 2:
        print("\nEntão pegue um guarda chuva, pois vai chover")
    if ceu == 3:
        print("\nVocê trouxe teu sabonete?")


condicao_ceu()

"""

While


Enquanto uma condição (é verdadeira / falsa / igual / maior / menor)

"""

# Comecei na 1, pois é a primeira linha a ser contada
seis_linhas = 1

while seis_linhas < 6:
    print(f"Linha {seis_linhas}... ainda não")
    seis_linhas += 1

if seis_linhas == 6:
    print(f"Linha {seis_linhas}... Agora sim!")


"""

Quando usar for e quando usar while

for: listas, ou range (1 a 10)

while: quando você não tem uma lista, um número fechado, não sabe (ou não se importa) com quantas vezes o 
código vai se repetir até que a condição estiver de acordo com o que deseja

"""

# Adivinhar o número que vai cair no dado


def errou():
    print(f"No dado caiu {aleatorio}")
    print("Tente de novo\n")
    exit()


def acertou():
    print(f"No dado caiu {aleatorio}")
    print("Parabéns, você acertou!!!\n")
    exit()


aleatorio = random.randint(1, 6)
escolhido = int(input("\nTente acertar o número que vai sair no dado: "))

while escolhido != aleatorio:
    errou()
while escolhido == aleatorio:
    acertou()
