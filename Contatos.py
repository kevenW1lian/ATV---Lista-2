import csv
import os

def criar_agenda(arquivo_csv):
    if not os.path.exists(arquivo_csv):
        with open(arquivo_csv, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Nome", "Telefone", "Email"])
    return arquivo_csv

def adicionar_contato(agendacsv, nome, telefone, email):
    with open(agendacsv, 'a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, telefone, email])
    print("Contato adicionado com sucesso!")

def listar_contatos(agendacsv):
    with open(agendacsv, 'r') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)  # Pule a primeira linha (cabeçalho)
        for row in reader:
            print(f"Nome: {row[0]} | Telefone: {row[1]} | Email: {row[2]}")

def buscar_contato(agendacsv, termo):
    with open(agendacsv, 'r') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)  # Pule a primeira linha (cabeçalho)
        encontrado = False
        for row in reader:
            if termo in row:
                print(f"Nome: {row[0]} | Telefone: {row[1]} | Email: {row[2]}")
                encontrado = True
        if not encontrado:
            print("Contato não encontrado.")

def remover_contato(agendacsv, termo):
    linhas = []
    with open(agendacsv, 'r') as arquivo:
        reader = csv.reader(arquivo)
        cabeçalho = next(reader)  # Obter o cabeçalho
        linhas.append(cabeçalho)
        for row in reader:
            if termo not in row:
                linhas.append(row)

    with open(agendacsv, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linhas)
    print("Contato removido com sucesso!")

def main():
    arquivo_csv = criar_agenda("agenda.csv")

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contato(arquivo_csv, nome, telefone, email)
        elif opcao == "2":
            listar_contatos(arquivo_csv)
        elif opcao == "3":
            termo = input("Digite o termo de busca: ")
            buscar_contato(arquivo_csv, termo)
        elif opcao == "4":
            termo = input("Digite o termo para remover: ")
            remover_contato(arquivo_csv, termo)
        elif opcao == "5":
            print("Encerrando a agenda.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
