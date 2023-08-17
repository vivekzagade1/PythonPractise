def factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact= fact*i
    return fact

def main():
    no = int(input('Enter the no: '))
    res = factorial(no)
    print(res)


if __name__ == "__main__":
    main()