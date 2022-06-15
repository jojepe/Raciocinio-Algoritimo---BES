import bd
import json


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


def sch_manga():
       while True:
        entry = str(input("Digite o nome do Mangá a ser pesquisado: "))
        if entry in bd.mangaBD:
            print("Mangá encontrado!")
            print(f"{entry}: {bd.mangaBD[entry]['Autor']}, {bd.mangaBD[entry]['Editora']}, R${(bd.mangaBD[entry]['Preço']):.2f} - "
                  f"{len(bd.mangaBD[entry]['Volumes'])} volumes.")
            break


def buy_manga():
    while True:
        entry = str(input("Insira o nome do Mangá a ser comprado: "))
        if entry in bd.mangaBD:
            print(f"{entry}")
        else:
            if input("O mangá " + str(entry) + " não foi encontrado! Deseja tentar novamente? (s/n)") == "n":
                break
        vol = int(input("Qual volume deseja comprar? "))
        num = int(input("Quantas unidades deseja adicionar ao carinho? "))
        bd.mangaBD.update()[entry]["Volumes"]["vol.1"][0] = 0
        print(bd.mangaBD)


def salvar_bd():
    bd_total = {
        'manga': bd.mangaBD,
        'clientes': bd.clientesBD,
        'carrinho': bd.carrinhoBD

    }
    with open("bd.json", "w") as file:
        json.dump(bd_total, file)


def resgatar_bd():
    with open('bd.json', 'r') as file:
        try:
            dados = json.load(file)
        except:
            return
        if dados is not None:
            bd.clientesBD = dados['clientes']
            bd.mangaBD = dados['manga']
            bd.carrinhoBD = dados['carrinho']

            
