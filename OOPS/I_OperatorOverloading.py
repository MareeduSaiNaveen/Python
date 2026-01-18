class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __add__(self, other):
        return Account("Total Balance", self.balance + other.balance)
    def __gt__(self, other):
        return self.balance > other.balance
    def __str__(self):
        return f"{self.name} : {self.balance}"
user1 = Account("Navin", 4000)
user2 = Account("Swathi", 6000)
total = user1 + user2
print(total)
if user1 > user2:
    print(f"{user1.name} has to pay bill")
else:
    print(f"{user2.name} has to pay bill")