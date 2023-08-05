import Marvellous

def main():
    value1 = int(input("Enter first no: "))
    value2 = int(input("Enter second no: "))

    res = 0

    res = Marvellous.Addition(value1, value2)
    print("Addition is: ", res)

    res = Marvellous.Substraction(value1, value2)
    print("Addition is: ", res)

    res = Marvellous.Multiplication(value1, value2)
    print("Addition is: ", res)

if __name__ == "__main__":
    main()