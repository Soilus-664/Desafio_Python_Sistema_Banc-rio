saldo = 0
limite_saque = 500 #por Dia
SAQUE_DIARIO = 3
saques = 0 
extrato = ""

menu = """

    [D] Deposito
    [S] Saque
    [E] Extrato
    [Q] Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "D":
        print("Deposito")

    elif opcao == "S":
        print("Saque")

    elif opcao == "E":
        print("Extrato")

    elif opcao == "Q": 
        break

    else:
        print("Opção Invalida, por favor selecione novamente uma opção valida! ")