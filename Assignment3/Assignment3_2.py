def acceptnumber():
    no = int(input("Enter nos of Elements: "))
    nos = []

    for i in range(0, no):
        nos.append(int(input(f"Enter the {i} element: ")))

    bignumber = nos[0]

    for i in range(0, no):
        if bignumber > nos[i]:
            bignumber = nos[i]

    print(bignumber)


def main():
    acceptnumber()


if __name__ == "__main__":
    main()
