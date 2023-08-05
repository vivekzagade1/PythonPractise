
def Addition(no1, no2):
    print(__name__)
    result = 0
    result = no1 + no2
    return result

def main():
    print(__name__)
    value1 = int(input("Enter First Number "))
    value2 = int(input("Enter Second Number "))

    answer = 0
    answer = Addition(value1, value2)

    print("Addition is : ", answer)

if __name__ == "__main__":  #starter
    main()