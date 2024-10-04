from datetime import date, datetime

import pytz

saldo = 0
limite_saque_diario = 500 #por Dia
saques = 0
transacoes = 0
TRANSACOES_DIARIAS = 10
SAQUE_DIARIO = 3
extrato = ""

data_atual = datetime.now(pytz.timezone("America/Sao_Paulo"))
mascara_ptbr = "%d/%m/%Y %H:%M"


menu = """
    [D] Deposito
    [S] Saque
    [E] Extrato
    [Q] Sair

=> """

def limite_de_transacoes():
    return transacoes == TRANSACOES_DIARIAS

def menu_extrato():
    
    def comeco_extrato_menu() :
        print(" Extrato ".center(50, "="))
    def final_extrato_menu():
        print("".center(50, "="))
    
    if extrato == "":
        comeco_extrato_menu()
        print(f"Nada Efetuado\n\nSaldo: {saldo:.2f}")
        final_extrato_menu()
    else:
        comeco_extrato_menu()
        print(f"{extrato}\nSaldo: {saldo:.2f}")
        final_extrato_menu()


def deposito():
    global saldo, extrato, exibir_extrato, transacoes
    deposito = float(input("insira o Valor do Deposito: "))
    
    if deposito > 0 and limite_de_transacoes() == False:
        saldo += deposito
        print(f"Deposito de {deposito:.2f} efetuado com sucesso!")
        extrato += f"Depósito: R${deposito:.2f}     Data: {data_atual.strftime(mascara_ptbr)}\n"
        transacoes += 1
    elif limite_de_transacoes() == True:
        print("Voce excedeu o limite de Transaçôes Diarias")
    else:
        print("A operação Falhou!")

def saque():
    global limite_saque_diario, SAQUE_DIARIO, saques, saldo, extrato, exibir_extrato, transacoes
    
    saque = float(input("insira o Valor do Saque: "))

    limite_de_saques_maximos = saques != SAQUE_DIARIO
    valor_positivo = saque > 0
    valor_maximo_de_saque = saque <= limite_saque_diario

    if valor_positivo and valor_maximo_de_saque and limite_de_saques_maximos and limite_de_transacoes() == False:
        if saque <= saldo:
            saldo -= saque
            print(f"Seu Saque de {saque:.2f} foi realizado com sucesso!")
            saques += 1
            extrato += f"Saque: R${saque:.2f}\n"
            transacoes += 1
        elif saque > saldo:
            print(f"Seu Saque de {saque:.2f} é maior que o seu Saldo {saldo:.2f}")
    elif valor_maximo_de_saque == False and limite_de_saques_maximos:
        print(f"O valor de Saque {saque:.2f} é maior que o Limite Diario {limite_saque_diario:.2f}")
    elif limite_de_saques_maximos == False:
        print("Voce excedeu o seu limite de Saques diarios")
    elif limite_de_transacoes() == True:
        print("Voce excedeu o limite de Transaçôes Diarias")
    else:
        print("A operação Falhou!")

while True:
    opcao = input(menu).upper()
    if opcao == "D":
        deposito()
    elif opcao == "S":
        saque()
    elif opcao == "E":
        menu_extrato()
        print(input("aperte [ENTER] para voltar ao menu"))
    elif opcao == "Q":
        break

    else:
        print("Opção Invalida, por favor selecione novamente uma opção valida! ")