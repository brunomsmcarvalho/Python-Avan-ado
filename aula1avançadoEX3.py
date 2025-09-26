class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor}€ realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor}€ realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        print(f"Saldo atual: {self.saldo}€")


conta = ContaBancaria("João", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.exibir_saldo()
conta.sacar(700)
conta.exibir_saldo()
conta.sacar(2000)
print("Saldo insuficiente, o seu saldo é:"),conta.exibir_saldo()
