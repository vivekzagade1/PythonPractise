def checkStart(no):
   
    for i in range(no):
       print("*",end=" ")
    print('')

def main():
    no = int(input('Enter the no: '))
    checkStart(no)


if __name__ == "__main__":
    main()