clientes = []

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