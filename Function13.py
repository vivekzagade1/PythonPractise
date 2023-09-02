
def demo(val1, val2):
    def add(a, b):
        return a + b

    return add(val1, val2)


def main():
    ret = demo(10, 7)

    print(ret)


if __name__ == '__main__':
    main()
