try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
except ValueError:
    print("Digite apenas números")
else:
    media = (nota1 + nota2 + nota3) / 3
    print(f"Sua média foi {media:.2f}")