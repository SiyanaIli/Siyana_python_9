class MessageLimiter:
    def __init__(self):
        self.limit = 10

    def add_limit(self, amount):
        self.limit += amount

    def send_message(self):
        if self.limit > 0:
            self.limit -= 1
        else:
            print("Message limit reached. Cannot send message.")

    def block_messages(self, amount):
        self.limit -= amount
        if self.limit < 0:
            self.limit = 0

    def show_limit(self):
        print(f"Remaining message limit: {self.limit}")
