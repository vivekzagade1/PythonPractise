class BankAccount:
    ROI = 10.5  # Class Variable

    def __init__(self, name, amount) -> None:  # Constructor
        self.amount = amount  # Instance Variable
        self.name = name

    def Display(self):  # Instance method
        print("Balance is : ", self.amount)
        print("Name is : ", self.name)

    def withdraw(self, val1):  # Instance method
        if self.amount < val1:
            print("Insufficient Funds")
        else:
            self.amount = self.amount - val1
            print("Amount withdrew success")

    def deposit(self, val1):  # Instance method
        self.amount += val1
        print("Deposit success")

    def calculateInterest(self):
        totalInterest = self.amount * (BankAccount.ROI / 100)
        print(totalInterest)


def main():
    obj1 = BankAccount("Hrishi", 4523)

    obj1.Display()
    obj1.deposit(564)
    obj1.Display()
    obj1.withdraw(455)
    obj1.Display()
    obj1.calculateInterest()


if __name__ == "__main__":
    main()
