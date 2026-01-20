class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_stock(self, quantity, amount):
        if quantity not in self.inventory:
            self.inventory[quantity] = {"available": 0, "reserved": 0}
        self.inventory[quantity]["available"] += amount

    def remove_stock(self, quantity, amount):
        if quantity in self.inventory and self.inventory[quantity]["available"] >= amount:
            self.inventory[quantity]["available"] -= amount
        else:
            print(f"Not enough available stock to remove for {quantity}.")

    def reserve_stock(self, quantity, amount):
        if quantity in self.inventory and self.inventory[quantity]["available"] >= amount:
            self.inventory[quantity]["available"] -= amount
            self.inventory[quantity]["reserved"] += amount
        else:
            print(f"Not enough available stock to reserve for {quantity}.")

    def show_stock(self, quantity):
        if quantity in self.inventory:
            counts = self.inventory[quantity]
            print(f"{quantity}: Available - {counts['available']}, Reserved - {counts['reserved']}")    
        else:
            print(f"No stock information for {quantity}.")    

