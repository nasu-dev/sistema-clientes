import json

clientes = []

def salvar():
    with open("clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)

def carregar():
    global clientes
    try:
        with open("clientes.json", "r") as arquivo:
            clientes = json.load(arquivo)
    except FileNotFoundError:
        clientes = []

def cadastrar():
    nome = input("Digite o nome: ").strip()
    telefone = input("Digite o telefone: ").strip()

    if not nome:
        print("Nome não pode ser vazio.")
        return

    if not telefone:
        print("Telefone não pode ser vazio.")
        return

    cliente = {
        "nome": nome,
        "telefone": telefone
    }

    clientes.append(cliente)
    salvar()
    print("Cliente cadastrado com sucesso!")

def listar():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i} - {cliente['nome']} | {cliente['telefone']}")

def editar():
    if not clientes:
        print("Nenhum cliente para editar.")
        return

    listar()

    try:
        indice = int(input("Digite o número do cliente que deseja editar: "))

        if indice < 1 or indice > len(clientes):
            print("Índice inválido.")
            return

        cliente = clientes[indice - 1]

        novo_nome = input(f"Novo nome ({cliente['nome']}): ")
        novo_telefone = input(f"Novo telefone ({cliente['telefone']}): ")

        if novo_nome:
            cliente['nome'] = novo_nome

        if novo_telefone:
            cliente['telefone'] = novo_telefone
        salvar()
        print("Cliente atualizado com sucesso!")

    except ValueError:
        print("Digite apenas números.")

def excluir():
    if not clientes:
        print("Nenhum cliente para excluir.")
        return

    listar()

    try:
        indice = int(input("Digite o número do cliente que deseja excluir: "))

        if indice < 1 or indice > len(clientes):
            print("Índice inválido.")
            return

        cliente_removido = clientes.pop(indice - 1)
        salvar()
        print(f"{cliente_removido['nome']} removido com sucesso!")

    except ValueError:
        print("Digite apenas números.")

carregar()

while True:
    print("==== Sistema de Clientes ====")
    print("1 - Cadastrar Clientes")
    print("2 - Editar Clientes")
    print("3 - Listar Clientes")
    print("4 - Excluir Clientes")
    print("0 - Sair")

    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if opcao == 0:
        break
    elif opcao == 1:
        cadastrar()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        listar()
    elif opcao == 4:
        excluir()