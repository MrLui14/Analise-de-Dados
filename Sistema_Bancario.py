menu = """

[1]Deposita
[2]Sacar
[3]Extrato
[4]Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
     
     opcao = input(menu)

     if opcao == "1":

        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"

        else:
            print("Operação falhou ! O valor informado é invalido")
     
     elif opcao == "2":
        
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
     
        excedeu_saques = valor >= LIMITE_SAQUE  
        
        if excedeu_saldo:
         print("Operação falhou! Você não tem saldo suficiente.")
        
        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
           print("Operação falhou! O valor informado é invalido.")
     elif opcao == "3":
        print("\n======== EXTRATO ========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================")
     
     elif opcao == "4":
        break
     
     else:
        print("Operação Invalida, por favor selecione novamente a operação desejada.")    