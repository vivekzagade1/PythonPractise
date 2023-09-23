
count = 0


def print_pattern(no):
    global count
    count += (no % 10)
    no = int(no / 10)
    if no != 0:
        print_pattern(no)
    else:
        print(count)
        return


def main():
    no = 4321
    print_pattern(no)


if __name__ == '__main__':
    main()
