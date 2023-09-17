import threading


def even(no):
    print(list(i*2 for i in range(1, no+1)))


def odd(no):
    print(list(1+(2*i) for i in range(0, no)))


def main():
    no = 10

    thread1 = threading.Thread(target=even, args=(no,))
    thread2 = threading.Thread(target=odd, args=(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == '__main__':
    main()
