def main():
    no = int(input('Enter the no'))
    for row in range(no+1):
        for col in range(no+1):
            if( row+col < no ):
                print('*', end=' ')
        print('')


if __name__ == "__main__":
    main()