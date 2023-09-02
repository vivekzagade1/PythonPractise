from functools import reduce


def checkPrime(no) -> bool:
    count = int(no/2) + 1
    counter = 2
    while(counter != count):
        if(no % counter == 0):
            return False
        counter += 1
    return True


def main():
    listO = []

    for i in range(8):
        listO.append(int(input(f'Enter {i} number: ')))
    print(listO)

    listf = list(filter(checkPrime, listO))
    print(listf)

    listm = list(map(lambda x: x * 2, listf))
    print(listm)

    listr = reduce(lambda x, y: x if x > y else y, listm)

    print(listr)


if __name__ == '__main__':
    main()
