def chkNum():
    no = int(input())
    
    if(no == 0 or no == 1):
        print("Neither odd or even")
        return

    if(no%2 == 0 and no!=0 and no!=1 ):
        print("Even Number")
    else:
        print("Odd Number")


def main():
    chkNum()


if __name__ == "__main__":
    main()