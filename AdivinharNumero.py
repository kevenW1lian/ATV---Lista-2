import random

# Gere um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

tentativas = 0

while True:
    tentativa = int(input("Digite a sua tentativa: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você adivinhou o número secreto ({numero_secreto}) em {tentativas} tentativas.")
        break
