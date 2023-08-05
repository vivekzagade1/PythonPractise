def checkEven(no):
    res = no % 2
    if(res == 0):
        print("even")
    else:
        print("odd")


def main():
    print("Enter no: ")
    no = int(input())

    checkEven(no)


if __name__ == "__main__":
    main()