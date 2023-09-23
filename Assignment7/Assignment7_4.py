import threading


def small_factor(no):
    count = 0
    for i in str(no):
        if(i.islower()):
            count += 1
    print(count)


def capital_factor(no):
    count = 0
    for i in str(no):
        if (i.isupper()):
            count += 1
    print(count)


def digit_factor(no):
    count = 0
    for i in str(no):
        if (i.isdigit()):
            count += 1
    print(count)


def main():
    no = "sadhbkahsdbDSFBIODFsdfdionUIFSDn5616F1MJFD45dfdf"

    thread1 = threading.Thread(target=small_factor, args=(no,))
    thread2 = threading.Thread(target=capital_factor, args=(no,))
    thread3 = threading.Thread(target=digit_factor, args=(no,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("Exit from main")


if __name__ == '__main__':
    main()
