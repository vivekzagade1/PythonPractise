def acceptnumber():
    no = int(input("Enter nos of Elements: "))
    nos = []

    for i in range(0, no):
        nos.append(int(input(f"Enter the {i} element: ")))

    bignumber = nos[0]

    count = 0
    searchElement = int(input("Elemtn to seach: "))
    for i in range(len(nos)):
        if(nos[i] == searchElement):
            count += 1
    print(count)


def main():
    acceptnumber()


if __name__ == "__main__":
    main()
