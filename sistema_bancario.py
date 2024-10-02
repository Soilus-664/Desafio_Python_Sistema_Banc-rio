saldo = 0
limite_saque_diario = 500 #por Dia
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
    deposito = float(input("insira o Valor do Deposito: "))
    
    if deposito > 0:
        saldo += deposito
        print(f"Deposito de {deposito:.2f} efetuado com sucesso!")
    else:
        print("A operação Falhou!")

def saque():
    global limite_saque_diario, SAQUE_DIARIO, saques, saldo
    
    saque = float(input("insira o Valor do Saque: "))

    if saque > 0 and saque <= limite_saque_diario and saques < SAQUE_DIARIO:
        if saque <= saldo:
            saldo -= saque
            print(f"Seu Saque de {saque:.2f} foi realizado com sucesso!")
            saques += 1
        elif saque > saldo:
            print(f"Seu Saque de {saque:.2f} é maior que o seu Saldo {saldo:.2f}")
    elif saque >= limite_saque_diario:
        print(f"O valor de Saque {saque:.2f} é maior que o Limite Diario {limite_saque_diario}")
    elif saques == SAQUE_DIARIO:
        print("Voce excedeu o seu limite de Saques diarios")
    else:
        print("A operação Falhou!")

while True:

    opcao = input(menu).upper()
    if opcao == "D":
        deposito()
    elif opcao == "S":
        saque()
    elif opcao == "E":
        print("Extrato")

    elif opcao == "Q":
        break

    else:
        print("Opção Invalida, por favor selecione novamente uma opção valida! ")