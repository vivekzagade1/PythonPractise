
count = 5


def print_pattern():
    global count
    print(count, end=" ")
    count -= 1
    if count != 0:
        print_pattern()
    else:
        print()
        return


def main():
    print_pattern()


if __name__ == '__main__':
    main()
