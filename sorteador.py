import random

def sorteio_numeros(inicial, final, quantidade):
    if inicial >= final or quantidade <= 0:
        print("Por favor, forneça valores válidos.")
        return

    numeros_sorteados = random.sample(range(inicial, final + 1), quantidade)
    print(f"Números sorteados entre {inicial} e {final}: {numeros_sorteados}")

# Exemplo de uso
inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))
quantidade = int(input("Digite a quantidade de números a sortear: "))

sorteio_numeros(inicial, final, quantidade)
