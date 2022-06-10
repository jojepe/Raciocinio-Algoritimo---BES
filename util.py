import bd


def rg_manga():
    while True:
        volumes = {}
        nome = (input("Insira o nome do Mangá: "))
        autor = str(input("Insira o nome do Autor: "))
        editora = str(input("Insira o nome da Editora: "))
        preco = float(input("Insira o valor de cada volume: "))
        num = int(input("Insira o número de volumes: "))
        for i in range(num):
            estoque = int(input("Insira o estoque do volume " + str(i + 1) + ": "))
            vol = "vol." + str(i + 1)
            volumes[vol] = estoque
        bd.mangaBD[nome] = {"Autor": autor, "Editora": editora, "Preço": preco, "Volumes": volumes}
        print(f"O mangá {nome}, {autor}, {editora}, {num} volumes - R${preco:.2f} foi adicionado com sucesso!")
        if input("Deseja adicionar mais um mangá? (s/n)") == "n":
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
    for k, v in bd.mangaBD.items():
        print(f"Mangá: {k}, " + str(len(v["Volumes"])) + " volumes  ----- R$" + str(v["Preço"]))


def rg_cliente():
    while True:
        nome = (input("Insira o nome do cliente: "))
        cpf = int(input("Insira o CPF do cliente: "))
        telefone = int(input("Insira o número de telefone do cliente: ((XX)-XXXX.XXXX) "))
        mail = str(input("Insira o e-mail do cliente: "))
        endereco = str(input("Insira o endereço do cliente: "))
        bd.clientesBD[cpf] = {"Nome": nome, "Telefone": telefone, "E-mail": mail, "Endereço": endereco}
        print(f"O cliente {nome} - CPF: {cpf},  Telefone: {telefone}, E-mail: {mail}, Endereço: {endereco} - foi adicionado com sucesso!")
        if input("Deseja adicionar mais um cliente? (s/n)") == "n":
            break

