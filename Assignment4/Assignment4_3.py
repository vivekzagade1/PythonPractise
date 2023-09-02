from functools import reduce


def main():
    listO = []

    for i in range(5):
        listO.append(int(input(f'Enter {i} number: ')))

    listf = list(filter(lambda x: 70 <= x <= 90, listO))
    listm = list(map(lambda x: x + 10, listf))

    listr = reduce(lambda x, y: x * y, listm, 0)

    print(listr)


if __name__ == '__main__':
    main()
