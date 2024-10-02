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

def deposito():
    global saldo
    deposito = int(input("insira o Valor do Deposito: "))
    saldo += deposito
    print(f"Deposito de {deposito} efetuado com sucesso!")

while True:

    opcao = input(menu).upper()
    if opcao == "D":
        deposito()

    elif opcao == "S":
        print("insira o Valor do Saque: ")

    elif opcao == "E":
        print("Extrato")

    elif opcao == "Q":
        break

    else:
        print("Opção Invalida, por favor selecione novamente uma opção valida! ")