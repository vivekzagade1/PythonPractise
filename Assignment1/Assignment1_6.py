def main():
    no = input("Enter no: ")
    
    if(no.isnumeric()):
        if(int(no) > 0 and int(no) != 0):
            print('Positive no')
        elif(int(no) < 0 and int(no) != 0):
            print('Negative no')
        else:
            print('Zero')
    else:
        print('Not number')


if __name__ == "__main__":
    main()