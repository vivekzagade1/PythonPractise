import threading


def even_factor(no):
    for i in range(2, int(no/2)+1):
        if(no % i == 0 and i % 2 == 0):
            print(i)


def odd_factor(no):
    for i in range(2, int(no/2)+1):
        if (no % i == 0 and i % 2 != 0):
            print(i)


def main():
    no = 45

    thread1 = threading.Thread(target=even_factor, args=(no,))
    thread2 = threading.Thread(target=odd_factor, args=(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")


if __name__ == '__main__':
    main()
