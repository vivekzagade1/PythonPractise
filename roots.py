import sys


def sqrt(x):

    if x < 0:
        raise ValueError(
            "Can't be less than zero"
            f"negative no: {x}")
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess


def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)

    print("Normal flow continues")


if __name__ == '__main__':
    main()
