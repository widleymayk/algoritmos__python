def produto_mais_barato():
    
    produto1 = float(input("Digite o preço do produto 1: R$ "))
    produto2 = float(input("Digite o preço do produto 2: R$ "))
    produto3 = float(input("Digite o preço do produto 3: R$ "))
    
    
    if produto1 < produto2 and produto1 < produto3:
        print("Compre o produto 1, pois é o mais barato.")
    elif produto2 < produto1 and produto2 < produto3:
        print("Compre o produto 2, pois é o mais barato.")
    elif produto3 < produto1 and produto3 < produto2:
        print("Compre o produto 3, pois é o mais barato.")
    else:
        print("Escolha o melhor.")


produto_mais_barato()