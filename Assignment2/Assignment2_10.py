def countNos(no):
    count = 0
    while(no != 0):
        digit = int(no%10)
        no = int(no /10)
        count+=digit
    return count



def main():
    no = int(input('Enter the nmber: '))
    count = countNos(no)
    print('Count is: ', count)


if __name__ == "__main__":
    main()