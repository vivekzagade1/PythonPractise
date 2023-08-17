def main():
    no = int(input('Enter the number: '))
    temp = int(no/2+1)
    count = 2
    while(count < temp):
        if(no%count == 0):
            print('Not Prime')
            return
        count+=1
    
    print('It is Prime')


if __name__ == "__main__":
    main()