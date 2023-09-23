import threading


def even_factor(no):
    count = 0
    for i in no:
        if(i % 2 == 0):
            count += i
    print(count)


def odd_factor(no):
    count = 0
    for i in no:
        if (i % 2 != 0):
            count += i
    print(count)


def main():
    no = [12, 54, 189, 49656, 95, 545, 92]

    thread1 = threading.Thread(target=even_factor, args=(no,))
    thread2 = threading.Thread(target=odd_factor, args=(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")


if __name__ == '__main__':
    main()
