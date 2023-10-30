# Taxas de câmbio fixas (a partir da moeda base)
taxas_cambio = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.72,
    "JPY": 110.46,
    "BRL": 5.00,
}

def converter_moeda(valor, moeda_origem, moeda_destino):
    if moeda_origem in taxas_cambio and moeda_destino in taxas_cambio:
        taxa_origem = taxas_cambio[moeda_origem]
        taxa_destino = taxas_cambio[moeda_destino]
        valor_convertido = valor * (taxa_destino / taxa_origem)
        return valor_convertido
    else:
        return "Moeda não suportada."

def main():
    while True:
        print("\nConversor de Moedas")
        print("Escolha uma opção:")
        print("1. Converter moeda")
        print("2. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            moeda_origem = input("Digite a moeda de origem (ex: USD, EUR, GBP, JPY): ").upper()
            moeda_destino = input("Digite a moeda de destino (ex: USD, EUR, GBP, JPY): ").upper()
            valor = float(input("Digite o valor a ser convertido: "))
            resultado = converter_moeda(valor, moeda_origem, moeda_destino)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"{valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")
        elif opcao == "2":
            print("Saindo do conversor de moedas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
