class Conta:
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo

    def imprimirSaldo(self):
        print("Saldo: R$ %.2f" % self.saldo)

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente para esta operação")
            return False

    def deposita(self, valor):
        self.saldo += valor

    def transfere(self, cc_destino, valor):
        if self.saca(valor) == True:
            cc_destino.deposita(valor)


# Código interativo
print("Bem-vindo ao sistema de contas!")
nome_cliente = input("Digite o nome do cliente: ")
numero_conta = input("Digite o número da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da conta: "))

conta = Conta(nome_cliente, numero_conta, saldo_inicial)

while True:
    print("\nOpções:")
    print("1. Consultar saldo")
    print("2. Realizar saque")
    print("3. Realizar depósito")
    print("4. Realizar transferência")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        conta.imprimirSaldo()
    elif opcao == "2":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        conta.saca(valor_saque)
    elif opcao == "3":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        conta.deposita(valor_deposito)
    elif opcao == "4":
        numero_destino = input("Digite o número da conta de destino: ")
        valor_transferencia = float(input("Digite o valor a ser transferido: "))
        conta_destino = Conta("Destino", numero_destino, 0)
        conta.transfere(conta_destino, valor_transferencia)
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, digite um número válido.")

       
