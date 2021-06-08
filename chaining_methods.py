class User:

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, amount, target):
        self.account_balance -= amount
        target.account_balance += amount
        self.display_user_balance()
        target.display_user_balance()

alex = User("Alex Franco", "alex@python.com")
juan = User("Juan Jones", "juan@python.com")
melanie = User("Melanie Castellanos", "melanie@python.com")
monica = User("Monica Trujillo", "monica@python.com")

print(alex.name)



alex.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance().transfer_money(50, melanie)

juan.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()

melanie.make_deposit(2000).make_withdrawal(500).make_withdrawal(500).make_withdrawal(200).display_user_balance()

