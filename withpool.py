import multiprocessing

def square(no):
    return no*no

def main():
    arr = [10, 20, 30, 40, 50]
    res = []

    p = multiprocessing.Pool()
    res = p.map(square, arr)
    p.close()
    p.join()

    print(res)

if __name__ == "__main__":
    main() 