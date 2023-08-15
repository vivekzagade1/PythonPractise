import time

def fun(no):
    sum = 0

    for i in range(100000):
        sum = sum + (no*no)

    return sum


def main():
    result = []

    starttime = time.time()

    for no in range(10000):
        result.append(fun(no))
    endtime = time.time()

    print(endtime - starttime)

if __name__ == "__main__":
    main()