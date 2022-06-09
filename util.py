import bd


def rg_manga():
    while True:
        manga = str(input("Digite o nome do Mangá: "))
        preco = float(input("Digite o preço do Mangá: "))
        estoque = int(input("Digite a quantidade do Mangá: "))
        bd.mangaPrecoBD[manga] = preco
        bd.mangaEstoqueBD[manga] = estoque
        if input("Deseja adicionar mais um Mangá? (s/n) ") == "n":
            break


def buy_manga():
    for k, v in bd.mangaEstoqueBD.items():
        while True:
            print(f"O manga {k} possui {v} cópias.")
            if input("Deseja adicionar o mangá ao carrinho? (s/n) ") == "s":
                print("Mangá colocado no carrinho com sucesso!")
                bd.mangaEstoqueBD[k] -= 1
                v -= 1
            else:
                break


def list_manga():
    for k, v in bd.mangaPrecoBD.items():
        print(f"Mangá: {k} ----- R${v}")

