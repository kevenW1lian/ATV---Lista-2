class CaixaEletronico:
    def __init__(self):
        self.saldo = 0

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}"
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}"
        elif valor <= 0:
            return "Valor de saque inválido."
        else:
            return "Saldo insuficiente."

def main():
    caixa = CaixaEletronico()

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar Saldo")
        print("2. Depositar Dinheiro")
        print("3. Sacar Dinheiro")
        print("4. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            saldo = caixa.consultar_saldo()
            print(f"Saldo atual: R${saldo:.2f}")
        elif opcao == "2":
            valor = float(input("Digite o valor a depositar: "))
            resultado = caixa.depositar(valor)
            print(resultado)
        elif opcao == "3":
            valor = float(input("Digite o valor a sacar: "))
            resultado = caixa.sacar(valor)
            print(resultado)
        elif opcao == "4":
            print("Saindo do caixa eletrônico.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
