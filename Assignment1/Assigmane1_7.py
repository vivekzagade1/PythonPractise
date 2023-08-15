def checkDiv5(no):
    if(no%5 == 0 and no != 0):
        print('True')
    else:
        print('False')

def main():
    no = int(input('Enter the no: '))
    checkDiv5(no)


if __name__ == "__main__":
    main()