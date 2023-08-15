import time
import multiprocessing

def fun(no):
    sum = 0

    for i in range(100000):
        sum = sum + (no*no)

    return sum


def main():
    result = []

    starttime = time.time()

    p = multiprocessing.Pool()

    result = p.map(fun, range(10000))

    p.close()
    p.join()

    endtime = time.time()

    print(endtime - starttime)

    #print(result)


if __name__ == "__main__":
    main()