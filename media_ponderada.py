numeroMaterias = int(input("Digite o número de matérias: "))

notas = []
pesos = []

for i in range(numeroMaterias):
    materia = input("Digite o nome da matéria: ")
    nota = float(input("Digite a nota da matéria: "))
    peso = float(input("Digite o peso da matéria: "))

    notas.append(nota)
    pesos.append(peso)

somaProdutos = sum([nota * peso for nota, peso in zip(notas, pesos)])
somaPesos = sum(pesos)
media = somaProdutos / somaPesos

print(f"A média ponderada é {media:.2f}")
