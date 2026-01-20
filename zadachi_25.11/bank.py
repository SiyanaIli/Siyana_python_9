class BankAccount:
    name=""
    balance=0.0
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "No no no"
        self.balance -= amount
        return self.balance
    
addi = BankAccount()
addi.name = "Addi"
addi.balance = 10000000000

jolly = BankAccount()
jolly.name = "Jolly"
jolly.balance = 500000000

print("ADDI's Account:")
print(addi.deposit(500))   
print(addi.withdraw(150)) 

print("JOLLY's Account:")
print(jolly.deposit(30))  
print(jolly.withdraw(100))  
