def calcular_media(vNota_um, vNota_dois, vNota_tres, vNota_quatro):
    return (vNota_um + vNota_dois + vNota_tres + vNota_quatro) / 4


vNota_um = float(input("Digite a primeira nota: "))
vNota_dois = float(input("Digite a segunda nota: "))
vNota_tres = float(input("Digite a terceira nota: "))
vNota_quatro = float(input("Digite a quarta nota: "))


vMedia = calcular_media(vNota_um, vNota_dois, vNota_tres, vNota_quatro)


print("A média é:", vMedia)
