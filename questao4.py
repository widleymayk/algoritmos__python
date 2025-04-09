
vogal = ['A', 'E', 'I', 'O', 'U']
consoante = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'X', 'Y', 'Z']

letra = input("Digite uma letra (para consoante ou vogal): ").upper()

if letra in vogal:
    print("A letra digitada é uma vogal.")
elif letra in consoante:
    print("A letra digitada é uma consoante.")
else:
    print("Você não digitou uma letra válida.")