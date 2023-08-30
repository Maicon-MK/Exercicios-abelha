
#2Defina uma classe BankAccount com atributos privados balance e account_number.
#Crie métodos deposit e withdraw para manipular o saldo.

class BankAccount:
    def __init__(self, balance, accountNumber):
        self.__balance = balance
        self.__accountNumber = accountNumber

    def deposit(self, dep):
        self.__balance += dep
        return self.__balance

    def withdraw(self, saq):
        if saq > self.__balance:
            print("Saldo insuficiente")
        else:
            self.__balance -= saq
            return saq


conta_1 = BankAccount(1000, "0006")

deposito = int(input("Quanto gostaria de depositar: "))
conta_1.deposit(deposito)
print("Saldo após depósito:", conta_1._BankAccount__balance)

saque = int(input("Quanto gostaria de sacar: "))
valor_sacado = conta_1.withdraw(saque)
if valor_sacado:
    print("Valor sacado:", valor_sacado)
    print("Saldo após saque:", conta_1._BankAccount__balance)

