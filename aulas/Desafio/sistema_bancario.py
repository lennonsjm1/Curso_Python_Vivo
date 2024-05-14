limite_saques = 3
valor_limite_diario = 500.0
saldo = 3000.0
total_sacado = 0
transacoes = []

def sacar():
    global saldo, total_sacado
    if total_sacado < limite_saques * valor_limite_diario:
        valor = float(input("Digite o valor a sacar: "))
        if valor <= saldo and (total_sacado + valor) <= limite_saques * valor_limite_diario:
            saldo -= valor
            total_sacado += valor
            transacoes.append(f"Saque: R${valor}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente ou limite diário atingido.")
    else:
        print("Limite diário de saques atingido.")

def depositar():
    global saldo
    valor = float(input("Digite o valor a depositar: "))
    saldo += valor
    transacoes.append(f"Depósito: R${valor}")
    print("Depósito realizado com sucesso!")

def ver_extrato():
    print(f"Saldo atual: R${saldo}")
    print("Transações:")
    for transacao in transacoes:
        print(transacao)

opcao = 0
while opcao != 4:
    print("\n[1] Sacar")
    print("[2] Depositar")
    print("[3] Ver Extrato")
    print("[4] Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        sacar()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        ver_extrato()
    elif opcao == 4:
        print("OBRIGADO E VOLTE SEMPRE")
    else:
        print("Opção inválida. Escolha uma opção de 1 a 4.")