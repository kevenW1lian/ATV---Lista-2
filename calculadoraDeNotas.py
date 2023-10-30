#Obter a nota correspondente com base na média
def obter_nota(media):
    if 90 <= media <= 100:
        return 'A'
    elif 80 <= media < 90:
        return 'B'
    elif 70 <= media < 80:
        return 'C'
    elif 60 <= media < 70:
        return 'D'
    else:
        return 'F'

#Solicitar o número de notas
num_notas = int(input("Quantas notas você deseja adicionar? "))

# Inicializar a soma das notas
soma_notas = 0

# Solicitar as notas para somar
for i in range(num_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma_notas += nota

# Calcular a média
media = soma_notas / num_notas

# Obter a nota correspondente
nota_correspondente = obter_nota(media)

# Exibir a média e a nota correspondente
print(f"Média das notas: {media}")
print(f"Nota correspondente: {nota_correspondente}")
