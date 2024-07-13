menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input("Digite o valor do depósito:"))

        if valor < 0:
            print("valor inválido")
        
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"

    elif opcao == 's':
        valor = float(input("Digite o valor do saque:"))

        if valor <= saldo and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Saque inválido")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break