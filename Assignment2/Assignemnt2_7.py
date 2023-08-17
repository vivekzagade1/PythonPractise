def main():
    no = int(input('Enter the no'))
    for row in range(1, no+1):
        for col in range(1, no+1):
                print(col, end=' ')
        print('')


if __name__ == "__main__":
    main()