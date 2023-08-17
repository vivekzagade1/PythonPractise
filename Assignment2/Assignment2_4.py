def main():
    no = int(input('Enter the number: '))
    temp = int(no/2+1)
    count = 0
    for i in range(1, temp):
        if(no%i == 0):
            count+=i
    print(count)


if __name__ == "__main__":
    main()