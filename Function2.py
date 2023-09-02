add = lambda a, b: a + b
sub = lambda a, b: a - b


def marvellous(val1, val2):
    ans1 = add(val1, val2)
    ans2 = sub(val1, val2)
    return ans1, ans2


def main():
    arr = marvellous(11, 7)
    print(arr)


if __name__ == '__main__':
    main()
