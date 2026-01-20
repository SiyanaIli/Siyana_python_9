class Wallet:
    def __init__(self, amount, currency):
        self.balance = amount
        self.currency = currency

    def add_money(self, amount):
        self.balance += amount

    def spend_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("no no no no money for you")

    def show_balance(self):
        print(f"{self.balance} {self.currency}")
