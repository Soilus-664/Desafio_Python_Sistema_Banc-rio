from datetime import date, datetime

import pytz, textwrap

def menu():
    def começo_menu():
        print(" MENU ".center(50, "="))
    
    {começo_menu()}
    print("\n[D] Deposito\n[S] Saque\n[C] Criar Usuário\n[F] Criar Conta\n[L] Listar Contas\n[E] Extrato\n[Q] Sair\n")    

def menu_extrato(saldo, /, *, extrato):
    def comeco_extrato_menu() :
        print(" Extrato ".center(50, "="))
    def final_menu():
        print("".center(50, "="))

    comeco_extrato_menu()
    print(f"Nada Efetuado\n\nSaldo: {saldo:.2f}") if extrato == "" else print(f"{extrato}\nSaldo: {saldo:.2f}")
    final_menu()

def deposito(saldo, valor, extrato, mascara_ptbr, /):    
    if valor > 0:
        saldo += valor
        print(f" Deposito de {valor:.2f} efetuado com sucesso! ".center(50,"="))
        extrato += f"Depósito: R${valor:.2f}\tData: {datetime.now(pytz.timezone("America/Sao_Paulo")).strftime(mascara_ptbr)}\n"
    else:
        print("A operação Falhou!")
    return saldo, extrato

def saque(*,saldo, valor, extrato, limite_saque_diario, SAQUE_DIARIO, saques, mascara_ptbr):
    limite_de_saques_maximos = saques != SAQUE_DIARIO
    valor_positivo = valor > 0
    valor_maximo_de_saque = valor <= limite_saque_diario

    if valor_positivo and valor_maximo_de_saque and limite_de_saques_maximos:
        if valor <= saldo:
            saldo -= valor
            print(f"Seu Saque de {valor:.2f} foi realizado com sucesso!")
            saques += 1
            extrato += f"Saque: R${valor:.2f}     Data: {datetime.now(pytz.timezone("America/Sao_Paulo")).strftime(mascara_ptbr)}\n"
        elif valor > saldo:
            print(f"Seu Saque de {valor:.2f} é maior que o seu Saldo {saldo:.2f}")
    elif valor_maximo_de_saque == False and limite_de_saques_maximos:
        print(f"O valor de Saque {valor:.2f} é maior que o Limite Diario {limite_saque_diario:.2f}".center(50, "="))
    elif limite_de_saques_maximos == False:
        print("Voce excedeu o seu limite de Saques diarios".center(50, "="))
    else:
        print("A operação Falhou!")
    return saldo, extrato

def criar_usuario(usuarios):    

    cpf = input("Informe o CPf (somente número): ")
    usuario = filtro_usuarios(cpf,usuarios)

    if usuario:
        print("\nEste CPF já está cadastrado!")
        return
    
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe a Data de Nascimento (dd-mm-yyyy)")
    endereco = input("Informe o endereço (Logradouro, n° - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(" Usuário criado com sucesso! ".center(50, "="))

def filtro_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe CPF do Usuario: ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print(" Conta criada com sucesso! ".center(50, "="))
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta errado!")

def listar_contas(contas):
    def menu_contas(conteudo):
        print(f" {conteudo} ".center(50,"="))
    
    for conta in contas:
        menu_contas("Contas")
        print(f"Agência:\t{conta["agencia"]}\nC/C:\t\t{conta["numero_conta"]}\nTitular:\t{conta["usuario"]["nome"]}")
        print("=" * 50)

def main():
    SAQUE_DIARIO = 3
    LIMITE_TRANSACOES = 10
    AGENCIA = "0001"

    saldo = 0   
    limite_saque_diario = 500 #por Dia
    saques = 0
    transacoes = 0
    extrato = ""
    usuarios = []
    contas = []
    
    mascara_ptbr = "%d/%m/%Y %H:%M:%S"
 
    while True:
        opcao = input(f"=> {menu()}").upper()

        if opcao == "D":
            if transacoes != LIMITE_TRANSACOES:
                valor = float(input("insira o Valor do Deposito: "))
                saldo, extrato = deposito(saldo, valor, extrato, mascara_ptbr)
                transacoes+=1
            else:
                print("Voce excedeu o limite de Transaçôes Diarias".center(50, "="))

        elif opcao == "S":
            if transacoes != LIMITE_TRANSACOES:
                valor = float(input("insira o Valor do Saque: ")) 
                saldo, extrato = saque(
                    saldo = saldo, 
                    valor = valor, 
                    extrato = extrato,
                    limite_saque_diario = limite_saque_diario,
                    SAQUE_DIARIO = SAQUE_DIARIO,
                    saques = saques,
                    mascara_ptbr = mascara_ptbr
                    )
                transacoes+=1
            else:
                print("Voce excedeu o limite de Transaçôes Diarias".center(50, "="))

        elif opcao == "C":  
            criar_usuario(usuarios)

        elif opcao == "F":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "L":
            listar_contas(contas)

        elif opcao == "E":
            menu_extrato(saldo, extrato = extrato)
            print(input("aperte [ENTER] para voltar ao menu"))

        elif opcao == "Q":
            break

        else:
            print("Opção Invalida, por favor selecione novamente uma opção valida! ")

main()