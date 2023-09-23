import threading


def even_factor():
    for i in range(1, 50):
        print(i)


def odd_factor():
    for i in range(50, 1, -1):
        print(i)


def main():
    thread1 = threading.Thread(target=even_factor, args=())
    thread2 = threading.Thread(target=odd_factor, args=())

    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()

    print("Exit from main")


if __name__ == '__main__':
    main()
