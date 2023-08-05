def main():
    
    no = 0
    print("Enter number: ")
    no = int(input())
    i = 1;
    while(i<(no/2)):
        if(no%i == 0):
            print(i)
        i+=1

if __name__ == "__main__":
    main()