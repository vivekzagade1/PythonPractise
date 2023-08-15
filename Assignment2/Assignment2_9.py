def countNos(no):
    count = 0
    while(no != 0):
        no = int(no /10)
        count+=1
    return count



def main():
    no = int(input('Enter the nmber: '))
    count = countNos(no)
    print('Count is: ', count)


if __name__ == "__main__":
    main()