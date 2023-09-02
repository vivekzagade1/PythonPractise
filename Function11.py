def marvellous(val1, val2):
    def add(a, b):
        return a + b

    ans = add(val1, val2)
    return ans


def main():
    ret = marvellous(11, 7)
    print(ret)


if __name__ == '__main__':
    main()
    