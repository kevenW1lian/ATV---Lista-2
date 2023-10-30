import json
import os

def carregar_tarefas(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            tarefas = json.load(arquivo)
        return tarefas
    else:
        return []

def salvar_tarefas(nome_arquivo, tarefas):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(tarefas, arquivo)

def adicionar_tarefa(tarefas, descricao):
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            status = "concluída" if tarefa["concluida"] else "pendente"
            print(f"{i}. [{status}] {tarefa['descricao']}")

def marcar_como_concluida(tarefas, numero_tarefa):
    if numero_tarefa >= 1 and numero_tarefa <= len(tarefas):
        tarefas[numero_tarefa - 1]["concluida"] = True
    else:
        print("Número de tarefa inválido.")

def remover_tarefa(tarefas, numero_tarefa):
    if numero_tarefa >= 1 and numero_tarefa <= len(tarefas):
        tarefas.pop(numero_tarefa - 1)
    else:
        print("Número de tarefa inválido.")

def main():
    nome_arquivo = "tarefas.json"
    tarefas = carregar_tarefas(nome_arquivo)

    while True:
        print("\nAplicativo de Gerenciamento de Tarefas")
        print("Escolha uma opção:")
        print("1. Listar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
            salvar_tarefas(nome_arquivo, tarefas)
            print("Tarefa adicionada com sucesso.")
        elif opcao == "3":
            listar_tarefas(tarefas)
            numero_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            marcar_como_concluida(tarefas, numero_tarefa)
            salvar_tarefas(nome_arquivo, tarefas)
        elif opcao == "4":
            listar_tarefas(tarefas)
            numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(tarefas, numero_tarefa)
            salvar_tarefas(nome_arquivo, tarefas)
        elif opcao == "5":
            print("Encerrando o aplicativo de gerenciamento de tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
