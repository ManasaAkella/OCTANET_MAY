class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def authenticate(self, user_id, pin):
        return self.user_id == user_id and self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient funds")

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, pin):
        self.users[user_id] = User(user_id, pin)

    def authenticate_user(self, user_id, pin):
        if user_id in self.users:
            return self.users[user_id].authenticate(user_id, pin)
        return False

    def get_user(self, user_id):
        if user_id in self.users:
            return self.users[user_id]
        return None


class Transaction:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

    def get_history(self):
        return self.history


class Main:
    @staticmethod
    def display_menu():
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    @staticmethod
    def perform_transaction(user, choice):
        if choice == 1:
            history = user.get_transaction_history()
            for transaction in history:
                print(transaction)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: $"))
            user.withdraw(amount)
        elif choice == 3:
            amount = float(input("Enter amount to deposit: $"))
            user.deposit(amount)
        elif choice == 4:
            recipient_id = input("Enter recipient's user ID: ")
            recipient = atm.get_user(recipient_id)
            if recipient:
                amount = float(input("Enter amount to transfer: $"))
                user.transfer(amount, recipient)
            else:
                print("Recipient not found")
        elif choice == 5:
            print("Exiting ATM...")
            return False
        return True


if __name__ == "__main__":
    atm = ATM()
    atm.add_user("123456", "1234")  

    user_id = input("Enter your user ID: ")
    pin = input("Enter your PIN: ")

    if atm.authenticate_user(user_id, pin):
        print("Authentication successful. Welcome!")
        user = atm.get_user(user_id)
        while True:
            Main.display_menu()
            choice = int(input("Enter your choice: "))
            if not Main.perform_transaction(user, choice):
                break
    else:
        print("Invalid user ID or PIN. Access denied.")
