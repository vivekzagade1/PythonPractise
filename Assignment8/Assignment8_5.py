
count = 1


def print_pattern(no):
    global count
    count *= no
    no -= 1
    if no != 0:
        print_pattern(no)
    else:
        print(count)
        return


def main():
    no = 5
    print_pattern(no)


if __name__ == '__main__':
    main()
