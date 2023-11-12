menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            pint("Operarcao invalida, valor informado e invalido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > valor
        excedeu_limite = valor > valor
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo o suficiente.")
        
        elif excedeu_limite:
            print("Operacao falhou! Valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operacao falhou! Numero maximo de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operacao falhou!")
    
    elif opcao == "e":
        print("\n         Extrato           ")
        print("nao foram realizados movimentacao." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print ("Operacao invalida.")








