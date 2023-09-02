def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def marvellous(FPTR1, FPTR2):
    ans = FPTR1(11, 12)
    print(ans)
    ans = FPTR2(11, 12)
    print(ans)


def main():
    marvellous(add, sub)


if __name__ == '__main__':
    main()
