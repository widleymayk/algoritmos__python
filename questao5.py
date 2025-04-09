def verificar_status_aluno(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media == 10:
        return f"Média: {media} - Aprovado com Distinção!"
    elif media >= 7:
        return f"Média: {media} - Aprovado!"
    else:
        return f"Média: {media} - Reprovado!"

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
print(verificar_status_aluno(nota1, nota2))