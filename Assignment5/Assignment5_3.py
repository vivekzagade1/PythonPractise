class Arithematic:
    pi = 3.14

    def __init__(self):
        self.val1 = 0
        self.val2 = 0
        self.add = 0
        self.sub = 0
        self.mul = 0
        self.div = 0

    def Accept(self):
        self.val1 = float(input('Enter the Val1: '))
        self.val2 = float(input('Enter the Val2: '))
        self.Addition()
        self.Subtraction()
        self.Multiplication()
        self.Division()
        self.Display()

    def Addition(self):
        self.add = self.val1 + self.val2

    def Subtraction(self):
        self.sub = self.val1 - self.val2

    def Multiplication(self):
        self.mul = self.val1 * self.val2

    def Division(self):
        self.div = self.val1 / self.val2

    def Display(self):
        print(self.add)
        print(self.sub)
        print(self.mul)
        print(self.div)


def main():
    obj1 = Arithematic()

    obj1.Accept()


if __name__ == '__main__':
    main()
