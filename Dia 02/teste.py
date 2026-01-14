# Pegando o valor total da conta
conta_final = int(input("Qual o valor da conta? "))

# Pegando qual a porcentagem da gorjeta
pergunta_gorjeta = int(input("Qual a porcentagem da gorjeta? 10, 15 ou 20? "))

# Pegando a quantidade de pessoas
pessoas = int(input("Para quantas pessoas a conta deve ser dividida? "))

# De acordo com o chat GPT, com o 1 antes, eu pego a porcentagem e somo com o cálculo (para nunca dar 0)
porcentagem_gorjeta = 1 + pergunta_gorjeta / 100


gorjeta = round(float((conta_final * porcentagem_gorjeta) / pessoas))

# print(f"Cada pessoa deve pagar: R${gorjeta:.2f}.")
print(f"Cada pessoa deve pagar: R${gorjeta}.")
