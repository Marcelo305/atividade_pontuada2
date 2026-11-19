import os
# 1. FUNÇÕES

def mostrar_saldo(saldo):
    print(f"Saldo atual: R$ {saldo}")

def depositar(saldo, extrato):
    valor = float(input("Valor do depósito: R$ "))
    if valor <= 0:
        print("Valor inválido! Informe um valor maior que zero.")
        return saldo
    saldo += valor
    extrato.append(f"Depósito: R$ {valor}")
    print("Depósito realizado!")
    return saldo

def sacar(saldo, extrato):
    valor = float(input("Valor do saque: R$ "))
    if valor <= 0:
        print("Valor inválido! Informe um valor maior que zero.")
        return saldo
    if valor > saldo:
        print("Saldo insuficiente!")
        return saldo
    saldo -= valor
    extrato.append(f"Saque: R$ {valor}")
    print("Saque realizado!")
    return saldo

def mostrar_extrato(extrato, saldo):
    if len(extrato) == 0:
        print("Nenhuma movimentação")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo}")

# 2. DADOS INICIAIS
saldo = 500
extrato = []

# 3. LAÇO DO MENU
while True:
    os.system("cls")
    print('''
=== BANCO COFRINHO ===
1- ver saldo
2- depositar
3- sacar
4- ver extrato
0- sair
''')
    opcao = int(input("Escolha uma opção: "))

    # 4. MATCH CASE
    match opcao:
        case 1:
            mostrar_saldo(saldo)
            input("pressione uma tecla para continuar")
        case 2:
            saldo = depositar(saldo, extrato)
            input("pressione uma tecla para continuar")
        case 3:
            saldo = sacar(saldo, extrato)
            input("pressione uma tecla para continuar")
        case 4:
            mostrar_extrato(extrato, saldo)
            input("pressione uma tecla para continuar")
        case 0:
            break
        case _:
            print("opçao invalida")
            input("pressione uma tecla para continuar")