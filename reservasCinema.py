import os

# Dicionário de filmes e horários
filmes = {
    1: {"nome": "Halloween", "horarios": ["10:00 AM", "14:30 PM", "19:00 PM"]},
    2: {"nome": "The Witch", "horarios": ["11:00 AM", "15:45 PM", "20:15 PM"]},
    3: {"nome": "Terrifier 2", "horarios": ["11:30 AM", "16:00 PM", "20:30 PM"]},
    4: {"nome": "Attack Of The Killer Donuts", "horarios": ["10:15 AM", "14:00 PM", "18:45 PM"]}
}

def mostrar_filmes():
    print("Filmes em exibição:")
    for chave, filme in filmes.items():
        print(f"{chave}. {filme['nome']}")

def mostrar_horarios(filme):
    print(f"Horários para '{filmes[filme]['nome']}':")
    for i, horario in enumerate(filmes[filme]["horarios"], start=1):
        print(f"{i}. {horario}")

def comprar_ingressos(filme, horario, quantidade):
    if filme in filmes and horario in range(1, len(filmes[filme]["horarios"]) + 1):
        try:
            with open("reservas.txt", "a") as arquivo:
                arquivo.write(f"Filme: {filmes[filme]['nome']}, Horário: {filmes[filme]['horarios'][horario - 1]}, Quantidade: {quantidade}\n")
            print(f"Ingressos comprados com sucesso para '{filmes[filme]['nome']}' às {filmes[filme]['horarios'][horario - 1]}.")
        except Exception as e:
            print(f"Erro ao comprar ingressos: {e}")
    else:
        print("Opção inválida. Verifique o número do filme e do horário.")

def main():
    while True:
        print("\nSistema de Reservas de Cinema")
        print("Escolha uma opção:")
        print("1. Mostrar filmes em exibição")
        print("2. Comprar ingressos")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            mostrar_filmes()
        elif opcao == "2":
            mostrar_filmes()
            filme = int(input("Escolha o número do filme: "))
            if filme in filmes:
                mostrar_horarios(filme)
                horario = int(input("Escolha o número do horário: "))
                quantidade = int(input("Digite a quantidade de ingressos desejada: "))
                comprar_ingressos(filme, horario, quantidade)
            else:
                print("Filme inválido.")
        elif opcao == "3":
            print("Saindo do sistema de reservas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
2
