def sub(a, b):
    if(a < b):
        a, b = b, a

    return a - b


def main():
    ret = sub(10, 7)
    print(ret)

    ret = sub(7, 10)
    print(ret)


if __name__ == '__main__':
    main()
