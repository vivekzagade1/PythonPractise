from functools import reduce


def main():
    listO = []

    for i in range(5):
        listO.append(int(input(f'Enter {i} number: ')))

    listf = list(filter(lambda x: x % 2 == 0, listO))
    print(listf)
    listm = list(map(lambda x: x * x, listf))
    print(listm)
    listr = reduce(lambda x, y: x + y, listm, 0)

    print(listr)


if __name__ == '__main__':
    main()
