class BankAccount():
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as f:
            self.balance = int(f.read())

    def deposit(self, amount):
        try:
            self.balance += int(amount)
            self.commit()
            self.view()
        except ValueError:
            print('There was a problem with the amount')

    def withdraw(self, amount):
        try:
            amount = int(amount)
            if self.balance <= amount:
                print('Not enough money in the account')
                self.view()
            else:
                self.balance -= amount
                self.commit()
                self.view()
        except ValueError:
            print('There was a problem with the amount')

    def view(self):
        print(self.balance)

    def commit(self):
        with open(self.filepath, 'w') as f:
            f.write(str(self.balance))


account = BankAccount('balance.txt')


class SavingBankAccount(BankAccount):
    def __init__(self, filepath, fee):
        BankAccount.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.withdraw(amount + self.fee)


test = SavingBankAccount('balance.txt', 1)
test.deposit(100)
test.transfer(100)
