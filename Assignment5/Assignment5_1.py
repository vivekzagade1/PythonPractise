class Demo:
    value = 0

    def __init__(self, val1, val2):
        self.no1 = val1
        self.no2 = val2

    def fun(self):
        print(self.no1)
        print(self.no2)

    def gun(self):
        print(self.no1)
        print(self.no2)


def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.gun()
    obj1.fun()
    obj2.gun()
    obj2.fun()


if __name__ == '__main__':
    main()
