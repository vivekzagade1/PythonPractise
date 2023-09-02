class Numbers:

    def __init__(self, value) -> None:  # Constructor
        self.value = value  # Instance Variable

    def factors(self):     # Instance method
        lis = []
        for i in range(1, int(self.value/2 + 1)):
            if(self.value % i == 0):
                lis.append(i)
        return lis

    def checkPrime(self) -> bool:
        count = int(self.value/2) + 1
        counter = 2
        while(counter == count):
            if(self.value % counter == 0):
                return True
            counter += 1
        return False

    def sumFactors(self):  # Instance method
        sumF = 0
        i = 1
        while(i < ((self.value / 2) + 1)):
            if(self.value % i == 0):
                sumF += i
            i += 1
        return sumF

    def checkPerfect(self):
        if(self.sumFactors() == self.value):
            return True
        return False


def main():
    obj1 = Numbers(6)
    print("Factors are: ", obj1.factors())
    print("Sum of factors are: ", obj1.sumFactors())
    print("Whether Prime: ", obj1.checkPrime())
    print("Whether perfect: ", obj1.checkPerfect())


if __name__ == "__main__":
    main()
