import random

def escolher_palavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip().lower()

def jogar_forca():
    palavra = escolher_palavra()
    palavra_oculta = ["_" if letra.isalpha() else letra for letra in palavra]
    tentativas = 6
    letras_usadas = []

    print("O jogo da Forca começou!")
    
    while True:
        print("\nPalavra: " + " ".join(palavra_oculta))
        print("Letras usadas: " + ", ".join(letras_usadas))
        print(f"Tentativas restantes: {tentativas}")
        
        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já escolheu essa letra. Tente outra.")
            continue

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas -= 1
        
        letras_usadas.append(letra)
        
        if "_" not in palavra_oculta:
            print("\nParabéns! Você ganhou! A palavra era: " + palavra)
            break
        
        if tentativas == 0:
            print("\nVocê perdeu! A palavra era: " + palavra)
            break

if __name__ == "__main__":
    jogar_forca()
