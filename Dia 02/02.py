# Dia 02 - Data types, Numbers, Operations, Type Conversion, f-Strings


"""
# Tipos de dados primitivos

String - Sequência de caracteres que representa texto / letras / símbolos

Integer - Números inteiros (positivos ou negativos)

Float - Números (positivos ou negativos) com vírgula, com casas decimais, que não são inteiros

Booleans - True ou False

"""

# Vai imprimir H (a letra na posição 0 da String)
print("Hello"[0])

# Vai imprimir o (a última letra da String)
print("Hello"[-1])


"""
123 = Int

"123" = String

"""

# Vai imprimir 123456 (está concatenando ao invés de somar, já que no caso são 2 strings)
print("123" + "456")

# Vai imprimir 579 (a soma entre os números inteiros 123 + 456)
print(123 + 456)

# Vai imprimir a penúltima letra do seu nome
teste = input("Digite teu nome: ")
print(teste[-2])


"""

Outra forma que escrever números inteiros é com _ (underline)

print(123_456_789_10)

Vai ser impresso como 

12345678910

Mas escrito como foi, irá facilitar a leitura (a máquina vai ignorar)


"""
# Print do exemplo acima
print(123_456_789_10)


# Float (número flutuante)
print(type(3.14159))

# Boolean
print(True)
print(False)


"""
len(12345)

Vai dar erro, pois len vai tentar contar a quantidade de caracteres numa string

Para imprimir, devemos primeiro transformar numa string

"""

print(len(str(123456)))

# Outra forma de contar quantos caracteres tem:
numero_grande = 12345665146843516841
strint_num = str(numero_grande)
print(len(strint_num))
# No caso acima, vai retornar 20, mas pode alterar se você adicionar / remover numeros

print("O número", numero_grande, "tem", len(strint_num), "caracteres.")


dado1 = "Olá"
dado2 = 29
dado3 = 29.07
dado4 = True


print(type(dado1))  # vai retonar str
print(type(dado2))  # vai retornar int
print(type(dado3))  # vai retornar float
print(type(dado4))  # vai retornar bool

"""
Passo 01: Define uma string
Passo 02: Converte a string para int
Passo 03: Printa o int
Passo 04: Printa o tipo da string convertida para int (para confirmar que realmente é int)


"""
teste01 = "324098"
teste02 = int(teste01)
print(teste02)
print(type(teste02))


"""
Exercício: Corrigir o código abaixo

print("Número de letras no seu nome: " + len(input("Digite seu nome: ")))

"""

print("Número de letras no seu nome: ", len(str(input("Digite seu nome: "))))


"""
Operações matemáticas

Adição  +
Subtração  -
Multiplicação  *
Divisão com resto  /
Divisão sem resto  //
Exponenciação **

"""

print(10 + 10)  # 20
print(20 - 10)  # 10
print(10 * 2)  # 20
print(30 / 3)  # 10.0 (tendo resto, e virando um float)
print(30 // 3)  # 10 (e vai descartar o final, permanecendo um int)
print(33 / 2)  # 16.5 (tendo resto, e virando um float)
print(type(33 / 2))  # para mostrar que muda para float
print(33 // 2)  # 16 (e vai descartar o final, permanecendo um int)
print(type(33 // 2))  # para mostrar que permanece um int
print(10**2)  # vai resultar em 10 * 10 que no caso será 100
print(10**3)  # vai resultar em 10 * 10 * 10 que no caso será 1000


""" 

Prioridade das opperações

Parenteses 
Exponenciação
Multiplicação ou Divisão (o que vier antes)
Adição ou Subtração o que vier antes


print(3 + (3**2) * 2)

Vai dar 21

1 - Será feito (3**2) que é a mesma coisa de 3 * 3
2 - Será feito o resultado da primeira conta * 2, que será 9 * 2 = 18
3 - Será pego o resultado da segunda conta e feito a última conta, que será 3 + 18 = 21

Se eu pegar a mesma conta e adicionar um -1 no final

print(3 + (3**2) * 2 - 1)

Vai dar 20

Segue a mesma regra de cima, porém como adição e subtração tem prioridade baixa, é efetuada a conta na ordem
que aparece (no caso primeiro a adição, depois a subtração)

"""
"""

Exercício: Alterar os sinais para a conta abaixo dar 3

print(3 * 3 + 3 / 3 + 3)

"""
# Solução Daniel
print(3 / 3 - 3 / 3 + 3)

# Solução do vídeo
print(3 * (3 + 3) / 3 - 3)

"""
Calculadora de IMC

O IMC serve para definir se alguém está acima ou abaixo do peso. É caluculado usando:

O IMC é igual o peso da pessoa dividido pela altura ao quadrado

Tendo em mente

altura = 1.65
peso = 84


"""
altura = 1.65
peso = 84
imc = peso / altura**2

print("O IMC é", imc)

"""
Round

Aproximação: Aproxima um número para cima ou para baixo, de acordo do que está mais perto

No exemplo da calculadora de IMC acima, o resultado deu

30.85399449035813

Para aproximar, podemos usar

print(round(imc))

Vai resultar em 31, porque 30.85... está mais perto de 31 do que 30

30.4 resultaria em 30


Também serve para exibir uma quantidade determinada de digitos. Ainda no resultado do IMC...

print(round(imc, 2))

Vai resultar em 30,85 (não será aproximado)

"""

print(round(imc))

print(round(imc, 2))


"""
Atribuição

# Número de gols iniciais numa partida
gol = 0

# Usuário marca um gol
gol +=1
print(gol)


________


Mário pegando moedas

moeda = 0
moeda += 1
varias = moeda + moeda + moeda
print("Seu número atual de moedas é", varias)

"""

gol = 0
gol += 1
print(gol)


moeda = 0
moeda += 1
varias = moeda + moeda + moeda
print("Seu número atual de moedas é", varias)

"""
f-String

É uma forma de facilitar a exibição de dados

Ainda no exemplo acima das moedas

Nome= Mario
Nacionalidade= Italiano
Moedas_pegas = varias

print(f"Olá! Meu nome é {Nome}, eu sou {Nacionalidade}, e nesse jogo já peguei {Moedas_pegas} moedas!")

"""

Nome = "Mario"
Nacionalidade = "Italiano"
Moedas_pegas = varias

print(
    f"Olá! Meu nome é {Nome}, eu sou {Nacionalidade}, e nesse jogo já peguei {Moedas_pegas} moedas!"
)

"""
Projeto final do dia: 

Calculadora de gorjetas

Pegar a conta final
Dar 3 opções de gorjeta 
Perguntar por quantas pessoas deve ser dividida a conta
Trazer o resultado



"""


# Pegando o valor total da conta
conta_final = int(input("Qual o valor da conta? "))

# Pegando qual a porcentagem da gorjeta
gorjeta = int(input("Qual a porcentagem da gorjeta? 10, 15 ou 20? "))

# Pegando a quantidade de pessoas
pessoas = int(input("Para quantas pessoas a conta deve ser dividida? "))

# De acordo com o Gemini, com o 1 antes, eu pego a porcentagem e somo com o cálculo (para nunca dar 0)
porcentagem = 1 + gorjeta / 100


gorjeta_final = round(float((conta_final * porcentagem) / pessoas))

# Colocando :.2f para mostrar apenas as duas casas decimais
print(f"Cada pessoa deve pagar: R${gorjeta_final}.")
