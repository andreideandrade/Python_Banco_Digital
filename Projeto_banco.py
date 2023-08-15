SISTEMA_BANCARIO = " Banco Digital "
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
OP_INVALIDA = "Operação falhou! "
VALOR_INVALIDO = "O valor informado é inválido"
MENU = '''

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        =>  '''
def titulo(titulo_nome):
    print(titulo_nome.center(50, "="))
    
def linha():
    for i in range(49):  
        print("", end="=")
    return "="

def op_invalida(informe_erro):
    print(f"Operação inválida! {informe_erro}.")
    
titulo(SISTEMA_BANCARIO)

while True:
    opcao = input(MENU)
    if opcao == "d" or opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            op_invalida(VALOR_INVALIDO)
    elif opcao == "s" or opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            op_invalida("Saldo insuficiente")
        elif excedeu_limite:
            op_invalida("O valor do saque excede o limite")
        elif excedeu_saques:
            op_invalida("Voce execedeu o numero de saques")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            op_invalida(VALOR_INVALIDO)
    elif opcao == "e" or opcao == "E":
        titulo(" EXTRATO ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(linha())
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(linha())
    elif opcao == "q" or opcao == "Q":
        break
    else:
        op_invalida("Por favor selecione novamente a operação desejada")

print(linha())
