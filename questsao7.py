
def encontrar_maior_menor():

    quantidade = int(input("Quantos números você quer inserir? "))

    
    maior = None
    menor = None

   
    for i in range(quantidade):
        numero = float(input(f"Digite o {i+1}º número: "))

        if maior is None or numero > maior:
            maior = numero
        
        if menor is None or numero < menor:
            menor = numero

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")


encontrar_maior_menor()
