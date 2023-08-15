def fun(no):
    sum = 0

    for i in range(10000):
        sum = sum + (no*no)

    return sum


def main():
    result = []

    for no in range(10000):
        result.append(fun(no))

if __name__ == "__main__":
    main()