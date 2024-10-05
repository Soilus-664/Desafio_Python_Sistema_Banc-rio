from datetime import date, datetime

import pytz

saldo = 0
limite_saque_diario = 500 #por Dia
saques = 0
transacoes = 0
TRANSACOES_DIARIAS = 10
SAQUE_DIARIO = 3
extrato = ""

mascara_ptbr = "%d/%m/%Y %H:%M:%S"

usuario = dict.fromkeys(["nome","data-de-nascimento","cpf","endereco"])

menu = """
    [D] Deposito
    [S] Saque
    [C] Criar Usuário
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

    final_extrato_menu() if usuario.get("nome") != None else ""
    print("Nome: {nome} CPF: {cpf}".format(**usuario)) if usuario.get("nome") != None else ""
    comeco_extrato_menu()
    print(f"Nada Efetuado\n\nSaldo: {saldo:.2f}") if extrato == "" else print(f"{extrato}\nSaldo: {saldo:.2f}")
    final_extrato_menu()

def deposito(valor: float):
    global saldo, extrato, transacoes
    
    if valor > 0 and limite_de_transacoes() == False:
        saldo += valor
        print(f"Deposito de {valor:.2f} efetuado com sucesso!")
        extrato += f"Depósito: R${valor:.2f}    Data: {datetime.now(pytz.timezone("America/Sao_Paulo")).strftime(mascara_ptbr)}\n"
        transacoes += 1
    elif limite_de_transacoes() == True:
        print("Voce excedeu o limite de Transaçôes Diarias")
    else:
        print("A operação Falhou!")

def saque(valor: float):
    global limite_saque_diario, SAQUE_DIARIO, saques, saldo, extrato, transacoes
    
    limite_de_saques_maximos = saques != SAQUE_DIARIO
    valor_positivo = valor > 0
    valor_maximo_de_saque = valor <= limite_saque_diario

    if valor_positivo and valor_maximo_de_saque and limite_de_saques_maximos and limite_de_transacoes() == False:
        if valor <= saldo:
            saldo -= valor
            print(f"Seu Saque de {valor:.2f} foi realizado com sucesso!")
            saques += 1
            extrato += f"Saque: R${valor:.2f}     Data: {datetime.now(pytz.timezone("America/Sao_Paulo")).strftime(mascara_ptbr)}\n"
            transacoes += 1
        elif valor > saldo:
            print(f"Seu Saque de {valor:.2f} é maior que o seu Saldo {saldo:.2f}")
    elif valor_maximo_de_saque == False and limite_de_saques_maximos:
        print(f"O valor de Saque {valor:.2f} é maior que o Limite Diario {limite_saque_diario:.2f}")
    elif limite_de_saques_maximos == False:
        print("Voce excedeu o seu limite de Saques diarios")
    elif limite_de_transacoes() == True:
        print("Voce excedeu o limite de Transaçôes Diarias")
    else:
        print("A operação Falhou!")

def criar_usuario():    
    global usuario

    usuario["nome"] = input("Digite o nome: ")
    usuario["data-de-nascimento"] = str(input("Digite sua data de nascimento: "))
    usuario["cpf"] = input("Digite o cpf: ")
    usuario["endereco"] = input("Digite o endereço: ")


while True:
    opcao = input(menu).upper()
    if opcao == "D":
        deposito(float(input("insira o Valor do Deposito: ")))
    elif opcao == "S":
        saque(float(input("insira o Valor do Saque: ")))
    elif opcao == "C":
        criar_usuario()
    elif opcao == "E":
        menu_extrato()
        print(input("aperte [ENTER] para voltar ao menu"))
    elif opcao == "Q":
        break
    else:
        print("Opção Invalida, por favor selecione novamente uma opção valida! ")