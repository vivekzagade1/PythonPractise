def acceptnumber():
    no = int(input("Enter nos of Elements: "))
    nos = []

    for i in range(0, no):
        nos.append(int(input(f"Enter the {i} element: ")))

    bignumber = 0

    for i in range(0, no):
        bignumber += nos[i]

    print(bignumber)


def main():
    acceptnumber()


if __name__ == "__main__":
    main()
