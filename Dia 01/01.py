# Dia 01 - Printing, commenting, debugging, Sting Manipulation and Variables

# função print imputa algo, uma mensagem

print('Hello world!')

# String é a mensagem que está entre os " " (no caso, a mensagem que será exibida, Hello world!)

'''

Para comentários, podemos usar três tipos

#

'''   '''

"""   """

Outra forma é selecionando e linha, e com o comando ctrl + /  (funciona com mais de uma linha selecionada por vez)

'''


"""
Exercício

Write a program that uses print statements to print the following recipe into the Output console. 
The text to print is already there, you just need to make it into code. Your code should print 
all five lines exactly the same as the example output below. Make sure that you don't change any 
of these existing text as everything, punctuation and casing all need to match!

1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.

"""

print('1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.')
print('2. Knead the dough for 10 minutes.')
print('3. Add 3g of Salt.')
print('4. Leave to rise for 2 hours.')
print('5. Bake at 200 degrees C for 30 minutes.')


# String Manipulation (como imputar várias linhas sem ter que ficar usando sempre o comando print individualmente)

# Para usso, podemos usar \n seguidamente

print('Hello World\nHello World!\nHello World!\nHello World')


"""

# Concatenar (juntar várias strings)

Você consegue juntar várias strings com o sinal de adição (lembrando que isso não adiciona espaços, então é interessante se for uma mensagem, 
criar uma string com espaço para melhorar a legibilidade)

print("Hello" + " " + "Daniel")

Você pode substituir o + por ,

print("Hello", "Daniel")

"""

print("Hello" + " " + "Daniel")


"""

Função input

Serve para interagir com o usuário (pegar nome, idade, informação)

"""

input('Qual seu nome?' + ' ')

print('Olá ' + input('Qual é seu nome? '))

'''
Exercício: Atualize o código para perguntar o nome da pessoa, e fazer uma saudação com uma exclamação no final

'''

print('Olá ' + input('Qual é seu nome? ') + '!')


"""
Armazenar variáveis

Onde guardamos informações para usar mais de uma vez (ou futuramente)

nome=input('Qual seu nome? ')
print(nome)

nome = "Daniel" # O resultado seria Daniel

"""


"""
Contando a quantidade de caracteres do meu nome

nome=input('Qual seu nome? ')
length=len(nome)
print(length)

Também pode ser

nome=input('Qual seu nome? ')
print('Seu nome tem', len(nome), 'caracteres!')

Assim não precisamos criar a variável length para contar, podemos mandar contar apenas o input


"""

nome=input('Qual seu nome? ')
length=len(nome)
print("Seu nome tem ", length, "caracteres")


print('Seu nome tem', len(nome), 'caracteres!')


"""

Exercício: Imprimindo o tamanho do meu nome enquanto pergunta


"""

print(len(input('Qual seu nome? ')))

"""
Trocar variáveis

Copo1 = "Leite"
Copo2 = "Suco"

Se eu quiser trocar, passar a ter as variáveis Suco no copo1 e Leite no copo2

Copo1, Copo2 = Copo2, Copo 1


"""

'''
Teste final da aula

Gerador de nome de banda

Crie um gerador de nome de banda, que cria um nome usando a cidade onde você nasceu e teu tipo de animal favorito

'''

print('Bem vindo ao Gerador de nome da bandas!!!')
cidade=input("Onde você nasceu?\n")
animal=input("Qual seu animal favorito?\n")
print('O nome da sua banda é:', animal, 'de', cidade, '.')