def main():
    
    no = 0
    print("Enter number: ")
    no = int(input())

    for i in range(1, int(no/2)):
        if(no%i == 0):
            print(i)

if __name__ == "__main__":
    main()