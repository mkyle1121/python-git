class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    '''
    This class generates checking account objects.
    '''
    type='checking'

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

a_checking = Checking('c:\\Users\\Mike Kyle\\PycharmProjects\\Mega Course\\account - class\\balance.txt',3)
a_checking.transfer(110)
#checking.deposit(10)
a_checking.commit()
print (a_checking.balance)
print(a_checking.type)

b_checking = Checking('c:\\Users\\Mike Kyle\\PycharmProjects\\Mega Course\\account - class\\balance.txt',3)
b_checking.transfer(110)
#checking.deposit(10)
b_checking.commit()
print (b_checking.balance)
print(b_checking.type)

print(Checking.__doc__)

# account = Account('c:\\Users\\Mike Kyle\\PycharmProjects\\Mega Course\\account - class\\balance.txt')
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.commit()

