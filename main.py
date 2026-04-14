clientes = []

def cadastrar():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")

    cliente = {
        "nome": nome,
        "telefone": telefone
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i} - {cliente['nome']} | {cliente['telefone']}")

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
        print(f"{cliente_removido['nome']} removido com sucesso!")

    except ValueError:
        print("Digite apenas números.")

while True:
    print("Bem vindo a *Clientes*")
    print("1 - Cadastrar Clientes")
    print("2 - Editar Clientes")
    print("3 - Listar Clientes")
    print("4 - Excluir clientes")
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
    elif opcao == 3:
        listar()
    elif opcao == 4:
        excluir()