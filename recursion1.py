import sys

i = 0


def fun():
    global i
    i += 1
    print(f"Recursion limit: {sys.getrecursionlimit()}, {i}")
    fun()


def main():
    fun()


if __name__ == '__main__':
    main()
