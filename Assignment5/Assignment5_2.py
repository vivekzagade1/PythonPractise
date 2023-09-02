class Circle:
    pi = 3.14

    def __init__(self):
        self.radius = 0
        self.area = 0
        self.circumference = 0

    def Accept(self):
        self.radius = float(input('Enter the Radius: '))
        self.CalculateArea()
        self.CalculateCircumference()
        self.Display()

    def CalculateArea(self):
        self.area = Circle.pi * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.pi * self.radius

    def Display(self):
        print(self.radius)
        print(self.area)
        print(self.circumference)


def main():
    obj1 = Circle()

    obj1.Accept()


if __name__ == '__main__':
    main()
