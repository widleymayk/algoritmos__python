def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")


vMetros = obter_numero("Digite a quantidade de metros: ")


vCentimetros = vMetros * 100


print(f"A quantidade de metros digitada em centímetros é: {vCentimetros} cm")
