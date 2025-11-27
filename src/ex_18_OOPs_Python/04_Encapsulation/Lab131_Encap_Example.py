class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number__ = account_number

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount

    # Our variables are encapsulated using methods which is known as encapsulation
    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number__)
        else:
            print("Not Allowed!")

icici = Bank(9876543210, 100)
icici.check_balance() # 100
icici.deposit(100)
icici.show_me_account_number(True)  # 9876543210
icici.check_balance() # 200
