
count = 1


def print_pattern():
    global count
    print(count, end=" ")
    count += 1
    if count != 6:
        print_pattern()
    else:
        print()
        return


def main():
    print_pattern()


if __name__ == '__main__':
    main()
